from chanfig import Config, Variable


class TestConfig(Config):
    __test__ = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        num_classes = Variable(10)
        self.name = "CHANfiG"
        self.seed = Variable(1013)
        self.network.name = "ResNet18"
        self.network.num_classes = num_classes
        self.dataset.num_classes = num_classes


class Test:

    config = TestConfig()

    def test_value(self):
        assert self.config.name == "CHANfiG"

    def test_nested(self):
        assert self.config.network.name == "ResNet18"

    def test_variable(self):
        assert self.config.network.num_classes == 10
        self.config.network.num_classes += 1
        assert self.config.dataset.num_classes == 11

    def test_fstring(self):
        assert f"seed{self.config.seed}" == "seed1013"

    def test_load(self):
        self.config.name = "Test"
        self.config.dataset.num_classes = 12
        self.config.dump("tests/test_config.json")
        self.config = self.config.load("tests/test_config.json")
        assert self.config.name == "Test"
        assert self.config.network.name == "ResNet18"
        assert self.config.network.num_classes == 12
        assert self.config.dataset.num_classes == 12
