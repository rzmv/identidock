import unittest
import identidock


class TestCase(unittest.TestCase):

    def setUp(self):
        identidock.app.config["TESTING"] = True
        self.app = identidock.app.test_client()

    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Max Razumov"))
        assert page.status_code == 200
        assert "Hello" in str(page.data)
        assert "Max Razumov" in str(page.data)
    
    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>OOOPS!</b><!--"'))
        assert '<b>' not in str(page.data)


if __name__ == "__main__":
    unittest.main()