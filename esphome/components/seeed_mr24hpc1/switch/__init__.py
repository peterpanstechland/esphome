import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import (
    DEVICE_CLASS_SWITCH,
    ENTITY_CATEGORY_CONFIG,
)
from .. import CONF_MR24HPC1_ID, mr24hpc1Component, mr24hpc1_ns

UnderlyingOpenFuncSwitch = mr24hpc1_ns.class_(
    "UnderlyOpenFunctionSwitch", switch.Switch
)

CONF_UNDERLY_OPEN_FUNCTION = "underly_open_function"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_MR24HPC1_ID): cv.use_id(mr24hpc1Component),
    cv.Optional(CONF_UNDERLY_OPEN_FUNCTION): switch.switch_schema(
        UnderlyingOpenFuncSwitch,
        device_class=DEVICE_CLASS_SWITCH,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon="mdi:electric-switch",
    ),
}


async def to_code(config):
    mr24hpc1_component = await cg.get_variable(config[CONF_MR24HPC1_ID])
    if underly_open_function_config := config.get(CONF_UNDERLY_OPEN_FUNCTION):
        s = await switch.new_switch(underly_open_function_config)
        await cg.register_parented(s, config[CONF_MR24HPC1_ID])
        cg.add(mr24hpc1_component.set_underly_open_function_switch(s))
