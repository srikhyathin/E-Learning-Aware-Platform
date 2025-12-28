from schemas import EngagementState

def adapt_content(emotion: str) -> EngagementState:
    if emotion == "happy":
        return EngagementState(
            emotion=emotion,
            interest=None,
            activity="continue_normal_flow"
        )

    if emotion == "bored":
        return EngagementState(
            emotion=emotion,
            interest="switch_to_visual_content",
            activity="show_images_videos"
        )

    if emotion == "confused":
        return EngagementState(
            emotion=emotion,
            interest=None,
            activity="slow_down_simplify"
        )

    return EngagementState(
        emotion=emotion,
        interest=None,
        activity="start_quiz_or_interactive"
    )
