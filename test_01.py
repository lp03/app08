import allure


class Test01:
    @allure.severity("blocker")
    @allure.step(title="这是第一个测试方法")
    def test_01(self):
        allure.attach("test_01", "这是test_01的步骤描述")
        assert 0

    @allure.severity("critical")
    @allure.step(title="这是第二个测试方法")
    def test_02(self):
        allure.attach("test_02", "这是test_02的步骤描述")
        assert 0

    @allure.severity("normal")
    @allure.step(title="这是第三个测试方法")
    def test_03(self):
        assert 1

    @allure.severity("minor")
    @allure.step(title="这是第四个测试方法")
    def test_04(self):
        assert 1

    @allure.severity("trivial")
    @allure.step(title="这是第五个测试方法")
    def test_05(self):
        assert 1
