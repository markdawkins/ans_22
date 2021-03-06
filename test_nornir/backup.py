from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir.core.filter import F

BACKUP_PATH = "./backups"

def backup_config(task, path):
    r = task.run(task=napalm_get, getters=["config"])
    task.run(
        task=write_file,
        content=r.result["config"]["running"],
        filename=f"{path}/{task.host}.txt",
    )

nr = InitNornir(config_file="./config.yml")

group = input("Enter group name(GROUP1,GROUP2,GROUP3,GROUP4,GROUP5,GROUP6) : ")

devices = nr.filter((F(groups__contains=(group))))


#devices = nr.filter(F(groups__contains="GROUP1"))

result = devices.run(
    name="Backup Device Configurations", path=BACKUP_PATH, task=backup_config
)

print_result(result, vars=["stdout"])
