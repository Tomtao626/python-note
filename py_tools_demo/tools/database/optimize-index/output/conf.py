from typing import AnyStr, List
import toml


def read_conf(conf_type: AnyStr) -> List:
	"""
	read conf
	:param conf_type: 配置类型
	:param conf_path: 配置文件地址
	:return: []
	"""
	config_path = "/Users/macos/Documents/workspaces/pywork/tools/database/optimize-index/output/config.toml"
	conf_reader = toml.load(config_path)['conf'][conf_type]
	print(conf_reader)
	return conf_reader
