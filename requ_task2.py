import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url=url, headers=headers, params=params).json()
        link = response['href']
        filename = file_path.split("/")
        data = open(filename[1], 'rb')
        upload_file = requests.put(link, data)
        if upload_file.status_code == 201:
            return f"Файл {filename[1]} успешно загружен в директорию /{filename[0]}/ на яндекс диск"

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = 'AQAAAAABNrQ-A ... '
    uploader = YaUploader(token)

    file_list = ['test.txt', 'test_1.txt']
    for filename in file_list:
        path_to_file = "test_file/" + filename
        result = uploader.upload(path_to_file)
        print(result)