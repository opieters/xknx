"""Module for XKNX Exception handling."""

from .exception import (
    CommunicationError,
    ConfirmationError,
    ConversionError,
    CouldNotParseAddress,
    CouldNotParseCEMI,
    CouldNotParseKNXIP,
    CouldNotParseTelegram,
    DataSecureError,
    DeviceIllegalValue,
    IncompleteKNXIPFrame,
    InvalidSecureConfiguration,
    IPSecureError,
    KNXSecureValidationError,
    ManagementConnectionError,
    ManagementConnectionRefused,
    ManagementConnectionTimeout,
    TunnellingAckError,
    UnsupportedCEMIMessage,
    XKNXException,
)

__all__ = [
    "CommunicationError",
    "ConfirmationError",
    "ConversionError",
    "CouldNotParseAddress",
    "CouldNotParseCEMI",
    "CouldNotParseKNXIP",
    "CouldNotParseTelegram",
    "DataSecureError",
    "DeviceIllegalValue",
    "IPSecureError",
    "IncompleteKNXIPFrame",
    "InvalidSecureConfiguration",
    "KNXSecureValidationError",
    "ManagementConnectionError",
    "ManagementConnectionRefused",
    "ManagementConnectionTimeout",
    "TunnellingAckError",
    "UnsupportedCEMIMessage",
    "XKNXException",
]
