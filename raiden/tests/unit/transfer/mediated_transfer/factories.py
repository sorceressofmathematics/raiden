# -*- coding: utf8 -*-
# pylint: disable=too-many-arguments
from raiden.utils import sha3
from raiden.transfer.state import (
    RouteState,
)
from raiden.transfer.mediated_transfer.state import (
    LockedTransferState,
)

# prefixing with UNIT_ to differ from the default globals
UNIT_SETTLE_TIMEOUT = 50
UNIT_REVEAL_TIMEOUT = 5
UNIT_TRANSFER_AMOUNT = 10

UNIT_SECRET = 'secretsecretsecretsecretsecretsecretsecr'
UNIT_HASHLOCK = sha3(UNIT_SECRET)

UNIT_TOKEN_ADDRESS = 'tokentokentokentokentokentokentokentoken'

ADDR = 'addraddraddraddraddraddraddraddraddraddr'
HOP1 = '1111111111111111111111111111111111111111'
HOP2 = '2222222222222222222222222222222222222222'
HOP3 = '3333333333333333333333333333333333333333'
HOP4 = '4444444444444444444444444444444444444444'
HOP5 = '5555555555555555555555555555555555555555'
HOP6 = '6666666666666666666666666666666666666666'

# add the current block number to get the expiration
HOP1_TIMEOUT = UNIT_SETTLE_TIMEOUT
HOP2_TIMEOUT = HOP1_TIMEOUT - UNIT_REVEAL_TIMEOUT
HOP3_TIMEOUT = HOP2_TIMEOUT - UNIT_REVEAL_TIMEOUT


def make_route(
        node_address,
        available_balance,
        settle_timeout=UNIT_SETTLE_TIMEOUT,
        reveal_timeout=UNIT_REVEAL_TIMEOUT,
        close_block=None,
        channel_address=None):
    """ Helper for creating a route.

    Args:
        node_address (address): The node address.
        available_balance (int): The available capacity of the route.
        settle_timeout (int): The settle_timeout of the route, as agreed in the netting contract.
        reveal_timeout (int): The configure reveal_timeout of the raiden node.
        channel_address (address): The correspoding channel address.
    """
    if channel_address is None:
        channel_address = ('channel' + node_address)[:40]

    state = 'available'
    route = RouteState(
        state,
        node_address,
        channel_address,
        available_balance,
        settle_timeout,
        reveal_timeout,
        close_block,
    )
    return route


def make_transfer(
        amount,
        target,
        expiration,
        secret=None,
        hashlock=UNIT_HASHLOCK,
        identifier=1):

    if secret is not None:
        assert sha3(secret) == hashlock

    transfer = LockedTransferState(
        identifier,
        amount,
        UNIT_TOKEN_ADDRESS,
        target,
        expiration,
        hashlock=hashlock,
        secret=secret,
    )
    return transfer
