from classes import *

if __name__ == '__main__':
    object_1 = VK(373712753)
    dict_photos = object_1.dict_photos_profile()

    object_2 = Yndex(TOKEN_YanD, dict_photos)
    object_2.upload_photos()
