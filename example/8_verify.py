from config import *
from glitter_sdk.util.encrypt.eth.ethereum import sha3
from glitter_sdk.core import PublicKey, EthSimplePublicKey
from glitter_sdk.core import (
    AccAddress,
)
from glitter_sdk.core.bech32 import get_bech
from coincurve import PublicKey


def verify(addr: str,msg: str,sign: str):
    pk = PublicKey.from_signature_and_message(bytes.fromhex(sign), msg.encode("utf-8"), sha3)
    ethKey = EthSimplePublicKey(pk.format(compressed=False).hex())
    addr1 = AccAddress(get_bech("glitter", ethKey.raw_address()))
    if addr1.lower() == addr.lower():
        return True
    else:
        return False


if __name__ == "__main__":
    mk = MnemonicKey("abc", 0, 0)
    m_str = "hello1"
    byteSign = mk.sign(m_str.encode("utf-8"))
    ok1 = verify(mk.acc_address,m_str,byteSign.hex())
    print(ok1)

    ok2 = verify(mk.acc_address, "hello2", byteSign.hex())
    print(ok2)

    mk3 = MnemonicKey("abc", 0, 1)
    ok3 = verify(mk.acc_address, "hello1",  mk3.sign(m_str.encode("utf-8")).hex())
    print(ok3)

