class SomeModel:
    def predict(self, message: str) -> float:
        value = 0.0
        if len(message) > 9:
            value = 1.0
        else:
            value = len(message) / 10
        return value


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if not 0 <= bad_thresholds <= 1 or not 0 <= good_thresholds <= 1 or\
       bad_thresholds > good_thresholds:
        return "Некорректные аргументы"

    value = model.predict(message)
    if value < bad_thresholds:
        return "неуд"
    if value > good_thresholds:
        return "отл"
    return "норм"
