from pathlib import Path
from typing import Any, Dict
import yaml


_ENDPOINT_CACHE: Dict[Path, Dict[str, Dict]] = {}

def _load_yaml_once(name) -> Dict[str, Any]:
    file_path = Path(__file__).parent / "source" / f"{name}.yaml"
    # Если уже загружали — возвращаем из кэша
    if file_path in _ENDPOINT_CACHE:
        return _ENDPOINT_CACHE[file_path]
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            if data is None:
                data = {}
            # Сохраняем в ГЛОБАЛЬНЫЙ кэш
            _ENDPOINT_CACHE[file_path] = data
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл конфигурации не найден: {file_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Ошибка чтения YAML-файла {file_path}: {e}")
    except PermissionError:
        raise PermissionError(f"Нет прав на чтение файла: {file_path}")
    

class EndpointsProvider:

    def __init__(self, name: str):
        self.endpoints_list = _load_yaml_once(name)

    
    def get_endpoint(self, servise_name, tag, endpoint_name) -> Dict:
        if tag not in self.endpoints_list: ValueError("Tag '{}' not found in file {}.yaml".format(tag, servise_name))
        if endpoint_name not in self.endpoints_list[tag]: ValueError("Endpoint '{}' of tag {} not found in file {}.yaml".format(endpoint_name, tag, servise_name))
        return self.endpoints_list[tag][endpoint_name]