from typing import Any
from dataclasses import dataclass
import json
@dataclass
class User:
    FirstName: str
    LastName: str
    UserName: str
    EmailId: str
    MobileNo: float
    isActive: bool
    OrgId: int
    UserId: int
    RoleId: int
    AuthStatus: bool
    Address1: str
    Address2: str
    City: str
    state: str
    country: str
    Pincode: int

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _FirstName = str(obj.get("FirstName"))
        _LastName = str(obj.get("LastName"))
        _UserName = str(obj.get("UserName"))
        _EmailId = str(obj.get("EmailId"))
        _MobileNo = float(obj.get("MobileNo"))
        _isActive = bool(obj.get("isActive"))
        _OrgId = int(obj.get("OrgId"))
        _UserId = int(obj.get("UserId"))
        _RoleId = int(obj.get("RoleId"))
        _AuthStatus =  bool(obj.get("AuthStatus"))
        _Address1 = str(obj.get("Address1"))
        _Address2 = str(obj.get("Address2"))
        _City = str(obj.get("City"))
        _state = str(obj.get("state"))
        _country = str(obj.get("country"))
        _Pincode = int(obj.get("Pincode"))
        return Root(_FirstName, _LastName, _UserName, _EmailId, _MobileNo, _isActive, _OrgId, _UserId, _RoleId, _AuthStatus, _Address1, _Address2, _City, _state, _country, _Pincode)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
