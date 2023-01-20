from psp.ml.models.yesterday import YesterdayPvSiteModel
from psp.ml.serialization import load_model, save_model


# Inheriting from some model to not have to implement all the methods like we would have to do if we
# defined one from scratch.
class TestModel(YesterdayPvSiteModel):
    def __init__(self):
        pass


def test_save_and_load(tmp_path):
    model = TestModel()
    path = tmp_path / "save_and_load.pkl"
    save_model(model, path)
    model2 = load_model(path)

    # Make sure it looks like a model!
    assert hasattr(model2, "predict")