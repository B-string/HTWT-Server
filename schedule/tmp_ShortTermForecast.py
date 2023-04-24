from enum import Enum
from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Category(Enum):
    PCP = "PCP"
    POP = "POP"
    PTY = "PTY"
    REH = "REH"
    SKY = "SKY"
    SNO = "SNO"
    TMN = "TMN"
    TMP = "TMP"
    TMX = "TMX"
    UUU = "UUU"
    VEC = "VEC"
    VVV = "VVV"
    WAV = "WAV"
    WSD = "WSD"


@dataclass
class Item:
    base_date: int
    base_time: str
    category: Category
    fcst_date: int
    fcst_time: str
    fcst_value: str
    nx: int
    ny: int

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        base_date = int(from_str(obj.get("baseDate")))
        base_time = from_str(obj.get("baseTime"))
        category = Category(obj.get("category"))
        fcst_date = int(from_str(obj.get("fcstDate")))
        fcst_time = from_str(obj.get("fcstTime"))
        fcst_value = from_str(obj.get("fcstValue"))
        nx = from_int(obj.get("nx"))
        ny = from_int(obj.get("ny"))
        return Item(base_date, base_time, category, fcst_date, fcst_time, fcst_value, nx, ny)

    def to_dict(self) -> dict:
        result: dict = {}
        result["baseDate"] = from_str(str(self.base_date))
        result["baseTime"] = from_str(self.base_time)
        result["category"] = to_enum(Category, self.category)
        result["fcstDate"] = from_str(str(self.fcst_date))
        result["fcstTime"] = from_str(self.fcst_time)
        result["fcstValue"] = from_str(self.fcst_value)
        result["nx"] = from_int(self.nx)
        result["ny"] = from_int(self.ny)
        return result


@dataclass
class Items:
    item: List[Item]

    @staticmethod
    def from_dict(obj: Any) -> 'Items':
        assert isinstance(obj, dict)
        item = from_list(Item.from_dict, obj.get("item"))
        return Items(item)

    def to_dict(self) -> dict:
        result: dict = {}
        result["item"] = from_list(lambda x: to_class(Item, x), self.item)
        return result


@dataclass
class Body:
    items: Items

    @staticmethod
    def from_dict(obj: Any) -> 'Body':
        assert isinstance(obj, dict)
        items = Items.from_dict(obj.get("items"))
        return Body(items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = to_class(Items, self.items)
        return result


@dataclass
class Response:
    body: Body

    @staticmethod
    def from_dict(obj: Any) -> 'Response':
        assert isinstance(obj, dict)
        body = Body.from_dict(obj.get("body"))
        return Response(body)

    def to_dict(self) -> dict:
        result: dict = {}
        result["body"] = to_class(Body, self.body)
        return result


@dataclass
class ShortTermForecast:
    response: Response

    @staticmethod
    def from_dict(obj: Any) -> 'ShortTermForecast':
        assert isinstance(obj, dict)
        response = Response.from_dict(obj.get("response"))
        return ShortTermForecast(response)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response"] = to_class(Response, self.response)
        return result


def short_term_forecast_from_dict(s: Any) -> ShortTermForecast:
    return ShortTermForecast.from_dict(s)


def short_term_forecast_to_dict(x: ShortTermForecast) -> Any:
    return to_class(ShortTermForecast, x)
