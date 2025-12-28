export default function LessonPane({ engagement }) {
  if (!engagement) return <p>Loading lesson...</p>;

  if (engagement.activity === "show_images_videos")
    return <p>Switched to visual content 👀</p>;

  if (engagement.activity === "slow_down_simplify")
    return <p>Explaining slowly with simpler examples ✨</p>;

  if (engagement.activity === "start_quiz_or_interactive")
    return <p>Let's try a quick interactive quiz! 🎯</p>;

  return <p>Continuing normal lesson 👍</p>;
}
