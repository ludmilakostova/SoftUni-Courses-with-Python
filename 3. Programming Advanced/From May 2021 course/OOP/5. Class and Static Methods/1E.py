class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.page_index = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        n_pages = photos_count//cls.PHOTOS_PER_PAGE
        return cls(n_pages)

    def is_space(self) -> bool:
        return self.page_index < self.pages and len(self.photos[self.page_index]) < PhotoAlbum.PHOTOS_PER_PAGE

    def page_new(self):
        if len(self.photos[self.page_index]) == PhotoAlbum.PHOTOS_PER_PAGE:
            self.page_index += 1
        return self.page_index

    def add_photo(self, label:str):
        if not self.is_space():
            return f'No more free slots'
        self.photos[self.page_index].append(label)
        p_added = f'{label} photo added successfully on page {self.page_index+1} slot {len(self.photos[self.page_index])}'
        self.page_new()
        return p_added

    def display(self):
        result = ""
        result += f"{11 * '-'}\n"
        for _ in self.photos:
            if _:
                result += "".join('[] ' for el in range(len(_))).strip()
            result += f'\n{11 * "-"}\n'
        return result


import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


if __name__ == "__main__":
    unittest.main()

