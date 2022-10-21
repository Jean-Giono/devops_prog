""" test modume """
import unittest
from webbrowser import get
import youtubepy
from os import path, getcwd


class TestYoutubeDownloader(unittest.TestCase):
    """ test class youtubedownloader """
    def test_get_infos(self):
        """ test get_infos method """
        vid_link1 = "https://youtu.be/HRNEi-xSNVA"
        vid_link2 = "https://youtu.be/OeZ_63iKPho"

        infos1 = youtubepy.get_infos(vid_link1)
        infos2 = youtubepy.get_infos(vid_link2)
        
        self.assertEqual(infos1[0], "Sommes-nous de plus en plus bêtes ? | 42, la réponse à presque tout | ARTE")
        self.assertEqual(infos1[1], "ARTE")
        self.assertNotEqual(infos1[2], "2022-05-29")

        self.assertEqual(infos2[1], "ScienceEtonnante")
        self.assertEqual(infos2[2], "2020-11-06")
        self.assertNotEqual(infos2[4], "2831")
	#self.assertEqual(infos2[3], "273702")

    def test_downloader(self):
        """ test downloader method """
        vid_link = "https://youtu.be/OjIcBraDKus"
        youtubepy.Downloader(vid_link)
        video_name = "Agnès Spiquel - Albert Camus Le Premier Homme.3gpp"
        file_exists = path.exists(getcwd()+"/"+video_name)
        self.assertTrue(file_exists)


if __name__ == '__main__':
    unittest.main()
