# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the strategy class."""
import logging
from random import randrange
from typing import Tuple

from temper import Temper

from aea.helpers.search.models import Description, Query
from aea.skills.base import SharedClass

from packages.fetchai.skills.thermometer.thermometer_data_model import (
    SCHEME,
    THERMOMETER_DATAMODEL,
)

DEFAULT_PRICE_PER_ROW = 1
DEFAULT_SELLER_TX_FEE = 0
DEFAULT_CURRENCY_PBK = "FET"
DEFAULT_LEDGER_ID = "fetchai"
DEFAULT_IS_LEDGER_TX = True
DEFAULT_HAS_SENSOR = True

logger = logging.getLogger(__name__)


class Strategy(SharedClass):
    """This class defines a strategy for the agent."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize the strategy of the agent.

        :param register_as: determines whether the agent registers as seller, buyer or both
        :param search_for: determines whether the agent searches for sellers, buyers or both

        :return: None
        """
        self._price_per_row = kwargs.pop("price_per_row", DEFAULT_PRICE_PER_ROW)
        self._seller_tx_fee = kwargs.pop("seller_tx_fee", DEFAULT_SELLER_TX_FEE)
        self._currency_id = kwargs.pop("currency_id", DEFAULT_CURRENCY_PBK)
        self._ledger_id = kwargs.pop("ledger_id", DEFAULT_LEDGER_ID)
        self.is_ledger_tx = kwargs.pop("is_ledger_tx", DEFAULT_IS_LEDGER_TX)
        self._has_sensor = kwargs.pop("has_sensor", DEFAULT_HAS_SENSOR)
        super().__init__(**kwargs)
        self._oef_msg_id = 0

    def get_next_oef_msg_id(self) -> int:
        """
        Get the next oef msg id.

        :return: the next oef msg id
        """
        self._oef_msg_id += 1
        return self._oef_msg_id

    def get_service_description(self) -> Description:
        """
        Get the service description.

        :return: a description of the offered services
        """
        desc = Description(SCHEME, data_model=THERMOMETER_DATAMODEL())
        return desc

    def is_matching_supply(self, query: Query) -> bool:
        """
        Check if the query matches the supply.

        :param query: the query
        :return: bool indiciating whether matches or not
        """
        # TODO, this is a stub
        return True

    def generate_proposal_and_data(self, query: Query) -> Tuple[Description, int]:
        """
        Generate a proposal matching the query.

        :param query: the query
        :return: a tuple of proposal and the temprature data
        """

        temp_data = self._build_data_payload()
        total_price = self._price_per_row
        assert (
            total_price - self._seller_tx_fee > 0
        ), "This sale would generate a loss, change the configs!"
        proposal = Description(
            {
                "price": total_price,
                "seller_tx_fee": self._seller_tx_fee,
                "currency_id": self._currency_id,
                "ledger_id": self._ledger_id,
            }
        )
        return proposal, temp_data

    def _build_data_payload(self) -> int:
        """
        Build the data payload.

        :param fetched_data: the fetched data
        :return: a tuple of the data and the rows
        """
        if self._has_sensor:
            temper = Temper()
            while True:
                results = temper.read()
                if "internal temperature" in results.keys():
                    degrees = results.get("internal temperature")
                else:
                    logger.debug("Couldn't read the sensor I am re-trying.")
        else:
            degrees = randrange(10, 25)

        return degrees
