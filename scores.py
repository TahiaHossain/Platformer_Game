from back_button import BackButton
from engine.label import Label
from engine.picocore import PicoCore
from engine.scene.scene import Scene
from score_system import ScoreSystem


def get_scores_scene(engine: PicoCore) -> Scene:
    score_scene = Scene(engine)

    score_scene.add_ui_object(
        Label(engine, "HIGH SCORES", (engine.width / 2), (engine.height / 2) + 100, alignment="center"))
    score_scene.add_ui_object(BackButton(engine, 40, engine.height - 40))

    score_system = ScoreSystem()

    high_scores = score_system.get_high_scores()

    for i in range(len(high_scores)):
        high_score = high_scores[i]
        score_label = Label(
            engine,
            f"{i + 1}. {high_score['score']}",
            (engine.width / 2),
            (engine.height / 2) - (i * 25),
            alignment="center"
        )
        score_scene.add_ui_object(score_label)
        print(high_score)

    return score_scene
