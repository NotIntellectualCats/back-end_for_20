import vk_api

with open("config_example.txt", "r") as F:
  token = F.readline()

session = vk_api.VkApi(token=token)

vk = session.get_api()




def mem(num):
  images = session.method("photos.get", {"owner_id": -197700721, "album_id": 281940823, "extended": 1})
  
  return images["items"][num]["sizes"][-1]["url"]
  
