import logging
import logging.handlers
import os

# Папка где лежит настоящий файл
LOG_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
# путь до клиентского лога
CLIENT_LOG_FILE_PATH = os.path.join(LOG_FOLDER_PATH, 'client.log')

# # Создаем именованный логгер с именем client
client_logger = logging.getLogger('client')
# устанавливаем уровень логгера
client_logger.setLevel(logging.INFO)

# обработчик будет логгер, который пишет в файл
client_handler = logging.FileHandler(CLIENT_LOG_FILE_PATH, encoding='utf-8')
# задаем уровень обработчика
client_handler.setLevel(logging.INFO)

# настраиваем форматтер вывода
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# связываем с форматером
client_handler.setFormatter(formatter)

# связываем с обработчиком
client_logger.addHandler(client_handler)

