import datetime
import typing

import pydantic

from pydantic import BaseModel, ValidationError, ConfigDict, Field, alias_generators
from src.utilities.formatters.datetime_formatter import format_datetime_into_isoformat
from src.utilities.formatters.field_formatter import format_dict_key_to_camel_case


class BaseSchemaModel(pydantic.BaseModel):
    # class Config(pydantic.BaseConfig):
    #     orm_mode: bool = True
    #     validate_assignment: bool = True
    #     allow_population_by_field_name: bool = True
    #     json_encoders: dict = {datetime.datetime: format_datetime_into_isoformat}
    #     alias_generator: typing.Any = format_dict_key_to_camel_case
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True,
        json_encoders= {datetime.datetime: format_datetime_into_isoformat},
        alias_generator=alias_generators.to_camel        
    )