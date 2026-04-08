# videoUtils.py
from manim import *
from manim_slides import Slide
import os


def load_frames(frame_dir, extensions=(".png", ".jpg", ".jpeg")):
    """Load and sort all image frames from a directory."""
    files = sorted(
        f for f in os.listdir(frame_dir)
        if f.lower().endswith(extensions)
    )
    return [ImageMobject(os.path.join(frame_dir, f)) for f in files]


def play_video_loop(
    scene: Slide,
    frame_dir: str,
    position=ORIGIN,
    height=None,
    width=None,
    fps=24,
    fade_in_time=0.5,
    fade_out_time=0.5,
    loop=True,
    persist=False,
):
    """
    Play a sequence of frames as a looping video inside a manim-slides Slide.

    Parameters
    ----------
    scene : Slide
        The current slide (pass `self` from within `construct`).
    frame_dir : str
        Path to the folder containing the frame images.
    position : np.ndarray
        Where to place the video center.
    height, width : float, optional
        Target size in scene units. If height is set, width is ignored.
    fps : int
        Playback rate.
    fade_in_time : float
        Duration of the fade-in on the first frame. 0 to skip.
    fade_out_time : float
        Duration of the fade-out after the loop. 0 to skip.
        Ignored when `persist=True`.
    loop : bool
        If True, wraps playback in a manim-slides loop segment.
    persist : bool
        If True, the last frame stays on screen and is returned as an
        ImageMobject you can animate further. If False, the video fades
        out (or is removed) and None is returned.

    Returns
    -------
    ImageMobject or None
        The last frame (still on scene) if `persist=True`, else None.
    """
    frames = load_frames(frame_dir)
    if not frames:
        raise ValueError(f"No frames found in {frame_dir}")

    # --- normalize size + position on every frame ---
    def _fit(f):
        if height is not None:
            f.height = height
        elif width is not None:
            f.width = width
        f.move_to(position)

    for f in frames:
        _fit(f)

    first = frames[0]
    dt = 1.0 / fps

    # --- fade in on the first frame ---
    first.set_opacity(0)
    scene.add(first)
    if fade_in_time > 0:
        scene.play(first.animate.set_opacity(1), run_time=fade_in_time)
    else:
        first.set_opacity(1)

    current = first

    # --- mark the loop region ---
    use_loop = loop and not persist
    if use_loop:
        scene.next_slide(loop=True)

    # --- play through frames ---
    for f in frames[1:]:
        scene.remove(current)
        scene.add(f)
        current = f
        scene.wait(dt)

    if loop:
        scene.next_slide()  # exits the loop segment

    # --- ending behavior ---
    if persist:
        # `current` is already on the scene, sized and positioned.
        # Return it so the caller can animate/move it further.
        return current

    if fade_out_time > 0:
        scene.play(current.animate.set_opacity(0), run_time=fade_out_time)
    scene.remove(current)
    return None

