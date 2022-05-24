# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2022 Valory AG
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
# flake8: noqa
# type: ignore
# pylint: skip-file
# To update; run: vulture aea --exclude "*_pb2.py" --make-whitelist > tests/whitelist.py
_.dependencies_highest_version  # unused property (aea/aea_builder.py:116)
_.set_search_service_address  # unused method (aea/aea_builder.py:484)
_.set_required_ledgers  # unused method (aea/aea_builder.py:850)
_.remove_private_key  # unused method (aea/aea_builder.py:580)
_.add_component_instance  # unused method (aea/aea_builder.py:643)
_.set_context_namespace  # unused method (aea/aea_builder.py:663)
_.remove_protocol  # unused method (aea/aea_builder.py:694)
_.remove_connection  # unused method (aea/aea_builder.py:714)
_.remove_skill  # unused method (aea/aea_builder.py:734)
_.remove_contract  # unused method (aea/aea_builder.py:754)
_.tick  # unused property (aea/agent.py:186)
AgentLoopException  # unused class (aea/agent_loop.py:134)
set_command  # unused function (aea/cli/config.py:53)
all_command  # unused function (aea/cli/list.py:47)
_.type_cast_value  # unused method (aea/cli/utils/click_utils.py:37)
_.get_metavar  # unused method (aea/cli/utils/click_utils.py:79)
_.convert  # unused method (aea/cli/utils/click_utils.py:83)
_.get_metavar  # unused method (aea/cli/utils/click_utils.py:100)
_.convert  # unused method (aea/cli/utils/click_utils.py:104)
_.convert  # unused method (aea/cli/utils/click_utils.py:129)
_.formatter  # unused attribute (aea/cli/utils/loggers.py:92)
is_item_present_unified  # unused function (aea/cli/utils/package_utils:394)
_.latest  # unused property (aea/configurations/base.py:384)
_.to_any  # unused property (aea/configurations/base.py:442)
_.to_latest  # unused property (aea/configurations/base.py:442)
_.to_uri_path  # unused property (aea/configurations/base.py:445)
_.to_uri_path  # unused property (aea/configurations/base.py:605)
_._ensure_connected  # unused method (aea/connections/base.py:104)
_._ensure_valid_envelope_for_external_comms  # unused method (aea/connections/base.py:109)
_._connect_context  # unused method (aea/connections/base.py:125)
_.has_crypto_store  # unused property (aea/connections/base.py:138)
_.from_dir  # unused method (aea/connections/base.py:200)
MyScaffoldAsyncConnection  # unused class (aea/connections/scaffold/connection.py:31)
_.get_instance  # unused method (aea/contracts/base.py:64)
_.from_dir  # unused method (aea/contracts/base.py:81)
_.get_raw_transaction  # unused method (aea/contracts/base.py:147)
_.get_raw_message  # unused method (aea/contracts/base.py:163)
MyScaffoldContract  # unused class (aea/contracts/scaffold/contract.py:25)
_.is_valid_address  # aea/crypto/cosmos.py:170: unused method 'is_valid_address' (60% confidence)
_.get_handle_transaction  # unused method (aea/crypto/cosmos.py:491)
_.execute_contract_query  # unused method (aea/crypto/cosmos.py:571)
_.get_code_id  # unused method (aea/crypto/cosmos.py:837)
_.get_contract_address  # unused method (aea/crypto/cosmos.py:849)
CosmosFaucetApi  # unused class (aea/crypto/cosmos.py:867)
testnet_name  # unused variable (aea/crypto/cosmos.py:871)
EthereumFaucetApi  # unused class (aea/crypto/ethereum.py:507)
testnet_name  # unused variable (aea/crypto/ethereum.py:511)
FetchAIFaucetApi  # unused class (aea/crypto/fetchai.py:404)
testnet_name  # unused variable (aea/crypto/fetchai.py:408)
_.has_ledger  # unused method (aea/crypto/ledger_apis.py:55)
_.get_api  # unused method (aea/crypto/ledger_apis.py:60)
_.has_spec  # unused method (aea/crypto/registries/base.py:236)
_.main_cryptos  # unused property (aea/crypto/wallet.py:130)
apply_delta  # unused method (aea/decision_maker/base.py:60)
is_initialized  # unused property (aea/decision_maker/base.py:70)
is_affordable_transaction  # unused method (aea/decision_maker/base.py:75)
apply_transactions  # unused method (aea/decision_maker/base.py:84)
list_of_terms  # unused variable (aea/decision_maker/base.py:85)
Preferences  # unused class (aea/decision_maker/base.py:98)
marginal_utility  # unused method (aea/decision_maker/base.py:118)
ownership_state  # unused variable (aea/decision_maker/base.py:119)
utility_diff_from_transaction  # unused method (aea/decision_maker/base.py:128)
ownership_state  # unused variable (aea/decision_maker/base.py:130)
logarithmic_utility  # unused function (/aea/helpers/preference_representations/base.py:28)
linear_utility  # unused function (/aea/helpers/preference_representations/base.py:55)
locate  # unused function (aea/helpers/base.py:139)
sigint_crossplatform  # unused function (aea/helpers/base.py:236)
_.dwFlags  # unused attribute (aea/helpers/base.py:269)
retry_decorator  # unused function (aea/helpers/base.py:386)
_.is_empty  # unused property (aea/helpers/dialogue/base.py:431)
_.self_initiated  # unused property (aea/helpers/dialogue/base.py:687)
_.other_initiated  # unused property (aea/helpers/dialogue/base.py:692)
_.add_dialogue_endstate  # unused method (aea/helpers/dialogue/base.py:697)
_.dialogue_stats  # unused property (aea/helpers/dialogue/base.py:767)
_.is_cancelled_by_timeout  # unused method (aea/helpers/exec_timeout.py:51)
exc_tb  # unused variable (aea/helpers/exec_timeout.py:102)
exc_type  # unused variable (aea/helpers/exec_timeout.py:102)
ExecTimeoutSigAlarm  # unused class (aea/helpers/exec_timeout.py:138)
envelope_from_bytes  # unused function (aea/helpers/file_lock.py:112)
LOCK_SH  # unused variable (aea/helpers/file_lock.py:32)
LOCK_NB  # unused variable (aea/helpers/file_lock.py:33)
_.filesize  # unused attribute (aea/helpers/ipfs/base.py:92)
MultiAddr  # unused class (aea/helpers/multiaddr/base.py:82)
_.in_path  # unused property (aea/helpers/pipe.py:70)
_.out_path  # unused property (aea/helpers/pipe.py:77)
_.in_path  # unused property (aea/helpers/pipe.py:171)
_.out_path  # unused property (aea/helpers/pipe.py:175)
_.in_path  # unused property (aea/helpers/pipe.py:305)
_.out_path  # unused property (aea/helpers/pipe.py:309)
make_ipc_channel  # unused function (aea/helpers/pipe.py:647)
make_ipc_channel_client  # unused function (aea/helpers/pipe.py:663)
to_set_specifier  # unused function (aea/helpers/pypi.py:199)
GenericDataModel  # unused class (aea/helpers/search/generic.py:29)
AGENT_LOCATION_MODEL  # unused variable (aea/helpers/search/generic.py:54)
AGENT_PERSONALITY_MODEL  # unused variable (aea/helpers/search/generic.py:61)
AGENT_SET_SERVICE_MODEL  # unused variable (aea/helpers/search/generic.py:71)
SIMPLE_SERVICE_MODEL  # unused variable (aea/helpers/search/generic.py:81)
SIMPLE_DATA_MODEL  # unused variable (aea/helpers/search/generic.py:88)
AGENT_REMOVE_SERVICE_MODEL  # unused variable (aea/helpers/search/generic.py:95)
_.counterparty_hash  # unused property (aea/helpers/transaction/base.py:529)
_.sender_payable_amount_incl_fee  # unused property (aea/helpers/transaction/base.py:598)
_.counterparty_payable_amount_incl_fee  # unused property (aea/helpers/transaction/base.py:623)
_.sender_fee  # unused property (aea/helpers/transaction/base.py:673)
_.counterparty_fee  # unused property (aea/helpers/transaction/base.py:679)
_.is_connecting  # unused attribute (aea/multiplexer.py:53)
_.put_message  # unused method (aea/multiplexer.py:821)
_.has_to  # unused property (aea/protocols/base.py:100)
ProtobufSerializer  # unused class (aea/protocols/base.py:278)
JSONSerializer  # unused class (aea/protocols/base.py:304)
_.from_dir  # unused method (aea/protocols/base.py:359)
INVALID_MESSAGE  # unused variable (aea/protocols/default/custom_types.py:30)
INVALID_DIALOGUE  # unused variable (aea/protocols/default/custom_types.py:32)
_.get_all_protocols  # unused method (aea/registries/resources.py:124)
_.remove_protocol  # unused method (aea/registries/resources.py:133)
_.get_contract  # unused method (aea/registries/resources.py:153)
_.get_all_contracts  # unused method (aea/registries/resources.py:165)
_.remove_contract  # unused method (aea/registries/resources.py:174)
_.get_connection  # unused method (aea/registries/resources.py:194)
_.remove_connection  # unused method (aea/registries/resources.py:215)
_.get_skill  # unused method (aea/registries/resources.py:248)
_.remove_skill  # unused method (aea/registries/resources.py:269)
_.get_all_handlers  # unused method (aea/registries/resources.py:309)
_.get_behaviour  # unused method (aea/registries/resources.py:318)
_.get_behaviours  # unused method (aea/registries/resources.py:331)
PUBLIC_ID  # unused variable (aea/skills/__init__.py:25)
_.agent_addresses  # unused property (aea/skills/base.py:154)
_.from_dir  # unused method (aea/skills/base.py:683)
CyclicBehaviour  # unused class (aea/skills/behaviours.py:57)
_.number_of_executions  # unused property (aea/skills/behaviours.py:66)
OneShotBehaviour  # unused class (aea/skills/behaviours.py:80)
TickerBehaviour  # unused class (aea/skills/behaviours.py:99)
_.last_act_time  # unused property (aea/skills/behaviours.py:135)
SequenceBehaviour  # unused class (aea/skills/behaviours.py:159)
FSMBehaviour  # unused class (aea/skills/behaviours.py:243)
_.is_started  # unused property (aea/skills/behaviours.py:258)
_.register_state  # unused method (aea/skills/behaviours.py:263)
_.register_final_state  # unused method (aea/skills/behaviours.py:280)
_.unregister_state  # unused method (aea/skills/behaviours.py:294)
_.final_states  # unused property (aea/skills/behaviours.py:331)
_.register_transition  # unused method (aea/skills/behaviours.py:364)
_.unregister_transition  # unused method (aea/skills/behaviours.py:383)
MyScaffoldBehaviour  # unused class (aea/skills/scaffold/behaviours.py:25)
MyScaffoldHandler  # unused class (aea/skills/scaffold/handlers.py:29)
MyModel  # unused class (aea/skills/scaffold/my_model.py:25)
_.is_executed  # unused property (aea/skills/tasks.py:68)
_.is_started  # unused property (aea/skills/tasks.py:146)
_.disable_aea_logging  # unused method (aea/test_tools/test_cases.py:134)
_.start_subprocess  # unused method (aea/test_tools/test_cases.py:198)
_.difference_to_fetched_agent  # unused method (aea/test_tools/test_cases.py:256)
_.delete_agents  # unused method (aea/test_tools/test_cases.py:328)
_.run_agent  # unused method (aea/test_tools/test_cases.py:341)
_.run_interaction  # unused method (aea/test_tools/test_cases.py:354)
_.is_successfully_terminated  # unused method (aea/test_tools/test_cases.py:407)
_.fingerprint_item  # unused method (aea/test_tools/test_cases.py:457)
_.eject_item  # unused method (aea/test_tools/test_cases.py:473)
_.run_install  # unused method (aea/test_tools/test_cases.py:488)
_.replace_private_key_in_file  # unused method (aea/test_tools/test_cases.py:549)
_.replace_file_content  # unused method (aea/test_tools/test_cases.py:596)
_.send_envelope_to_agent  # unused method (aea/test_tools/test_cases.py:685)
_.read_envelope_from_agent  # unused method (aea/test_tools/test_cases.py:694)
_._is_teardown_class_called  # unused attribute (aea/test_tools/test_cases.py:801)
_._start_oef_node  # unused method (aea/test_tools/test_cases.py:808)
network_node  # unused variable (aea/test_tools/test_cases.py:809)
_.get_dialogues_with_counterparty  # unused method (aea/protocols/dialogue/base.py:999)
receiver_address  # unused variable (aea/decision_maker/default.py:70)
receiver_address  # unused variable (aea/decision_maker/default.py:99)
create_with_message  # unused method (aea/helpers/dialogue/base.py:1054)
_.is_disconnecting  # unused property (aea/multiplexer.py:67)
_.get_quantity_in_outbox  # unused method (aea/test_tools/test_skills.py:52)
_.get_message_from_outbox  # unused method (aea/test_tools/test_skills.py:56)
_.drop_messages_from_outbox  # unused method (aea/test_tools/test_skills.py:70)
_.drop_messages_from_decision_maker_inbox  # unused method (aea/test_tools/test_skills.py:86)
_.get_quantity_in_decision_maker_inbox  # unused method (aea/test_tools/test_skills.py:69)
_.get_message_from_decision_maker_inbox  # unused method (aea/test_tools/test_skills.py:73)
_.assert_quantity_in_outbox  # unused method (aea/test_tools/test_skills.py:79)
_.assert_quantity_in_decision_making_queue  # unused method (aea/test_tools/test_skills.py:86)
_.message_has_attributes  # unused method (aea/test_tools/test_skills.py:69)
_.build_incoming_message_for_skill_dialogue  # unused method (aea/test_tools/test_skills.py:155)
_.prepare_skill_dialogue  # unused method (aea/test_tools/test_skills.py:290)
_.__defaults__  # unused attribute (aea/protocols/dialogue/base.py:49)
_.build_incoming_message_for_dialogue  # unused method (aea/test_tools/test_skills.py:155)
_._has_message  # unused method (aea/protocols/dialogue/base.py:491)
MultiAgentManager  # unused class (aea/manager.py:127)
_.add_error_callback  # unused method (aea/manager.py:202)
_.start_manager  # unused method (aea/manager.py:208)
_.stop_manager  # unused method (aea/manager.py:221)
_.projects  # unused property (aea/manager.py:228)
_.add_project  # unused method (aea/manager.py:263)
_.list_projects  # unused method (aea/manager.py:283)
_.list_agents_info  # unused method (aea/manager.py:283)
_.add_agent  # unused method (aea/manager.py:291)
_.start_all_agents  # unused method (aea/manager.py:396)
_.get_agent_alias  # unused method (aea/manager.py:486)
_.DEFAULT_PYPI_INDEX_URL  # unused variable (aea/configurations/base.py:85)
AEARunner  # unused class (aea/runner.py:84)
_.join_thread  # unused method (aea/helpers/multiple_executor.py:430)
_.valid_performatives  # unused property (aea/protocols/base.py:90)
_.has_dialogue_info  # unused property (aea/protocols/base.py:244)
get_state  # aea/crypto/base.py:251: unused method 'get_state' (60% confidence)
_.load_agent_config  # unused method (aea/test_tools/test_cases.py:801)
_.UseGanache  # unused class (aea/test_tools/test_cases.py:871)
_._start_ganache  # unused method (aea/test_tools/test_cases.py:875)
_.ganache  # unused variable (aea/test_tools/test_cases.py:876:)
_.unsupported_protocol_count
_.unsupported_skill_count
_.decoding_error_count
_.ErrorHandler  # unused class (aea/error_handler/scaffold.py:27)
ensure_dir  # unused function (aea/helpers/base.py:561)
_.get_agent_overridables  # unused method (aea/manager/manager.py:419)
_.set_agent_overrides  # unused method (aea/manager/manager.py:432)
by_path  # unused function (aea/cli/fingerprint.py:94)
AgentRecord  # unused class (aea/helpers/acn/agent_record.py:49)
check_validity  # unused method (aea/helpers/acn/agent_record.py:96)
signature_from_cert_request  # unused function (aea/helpers/acn/agent_record.py:51)
Uri  # unused class (aea/helpers/acn/uri.py:26)
not_before_string  # unused property (aea/helpers/base.py:724)
not_after_string  # unused property (aea/helpers/base.py:729)
from_cert_request  # unused method (aea/helpers/acn/agent_record.py:136)
FetchAICrypto  # unused class (aea/crypto/fetchai.py:40)
entity  # unused property (aea/crypto/base.py:77)
callable_name  # unused variable (aea/crypto/base.py:277)
update_with_gas_estimate  # unused method (aea/crypto/base.py:362)
try_decorator  # unused function (aea/helpers/base.py:284)
from_string  # unused method (aea/helpers/multiaddr/base.py:163)
BaseSyncConnection  # unused class (aea/connections/sync_connection.py:33)
_.put_envelope  # unused method (aea/connections/sync_connection.py:84)
MyScaffoldSyncConnection  # unused class (aea/connections/scaffold/connection.py:89)
run_count  # unused variable (aea/test_tools/test_cases.py:998)
_.get_addresses  # unused method (aea/manager/project.py:284)
_.get_connections_addresses  # unused method (aea/manager/project.py:289)
_.check_protobuf_using_protoc  # unused function (aea/protocols/generator/common.py:420)
_.last_start_status  # unused property (aea/manager/manager.py:296)
from_uri_path  # unused method (aea/configurations/data_types.py:339)
from_uri_path  # unused method (aea/configurations/data_types.py:497)
no_active_handler_count  # unused attribute (aea/error_handler/default.py:76)
parse_module  # unused method (aea/skills/base.py:359)
parse_module  # unused method (aea/skills/base.py:419)
parse_module  # unused method (aea/skills/base.py:463)
parse_module  # unused method (aea/skills/base.py:520)
_.__path__  # unused attribute (aea/components/base.py:137)
_.__path__  # unused attribute (aea/components/base.py:140)
_.__path__  # unused attribute (aea/components/base.py:143)
short_help  # unused method (aea/cli/plugin.py:83)
parse_args  # unused method (aea/cli/plugin.py:99)
encrypt  # unused method (aea/crypto/base.py:148)
decrypt  # unused method (aea/crypto/base.py:158)
keyfile_json  # unused variable (aea/crypto/base.py:159)
DecryptError  # unused class (aea/crypto/helpers.py:195)
hex_to_bytes_for_key  # unused function (aea/crypto/helpers.py:209)
item_owner_crypto  # unused attribute 'item_owner_crypto' (aea/test_tools/test_contract.py:70)
TCPSocketChannelClientTLS  # unused class (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/pipe.py:597)
_.check_hostname  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/pipe.py:603)
_.verify_mode  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/pipe.py:604)
_.last_exception  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/pipe.py:539)
_.last_exception  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/pipe.py:567)
_.last_exception  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/pipe.py:630)
_.last_exception  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/pipe.py:649)
run_install_subprocess  # unused function (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/install_dependency.py:75)
_.deployment_tx_receipt  # unused attribute (agents-aea/aea/test_tools/test_contract.py:105)
_.Hash  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/ipfs/base.py:124)
_.Tsize  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/ipfs/base.py:125)
_.Name  # unused attribute (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/ipfs/base.py:126)
init_worker  # unused function (/home/solarw/MyData/work/fetchai/agents-aea/aea/skills/tasks.py:108)
_._generate_hash  # unused method (/home/solarw/MyData/work/fetchai/agents-aea/aea/helpers/ipfs/base.py:161)
register_item_to_local_registry  # unused function in (aea/cli/registry/ipfs.py:59)
find_item_in_distribution  # unused function in (aea/cli/utils/package_utils.py:353)
is_distributed_item  # unused function in (aea/cli/utils/package_utils.py:618)
PACKAGE_TYPE_TO_CONFIG_FILE  # unused variable in (aea/configurations/constants.py:90)
raise_on_try  # unused variable (aea/crypto/base.py:383)
fetch_item_mixed  # unused function (aea/cli/add.py:241)
DEFAULT_IPFS_URL  # unused variable (aea/cli/registry/settings.py:49)
get_registry_config  # unused function (aea/cli/utils/config.py:156)
dump_yaml  # unused function (aea/helpers/dependency_tree.py:58)
DependecyTree  # unused class (aea/helpers/dependency_tree.py:104)
generate_all  # unused function (aea/cli/ipfs_hash.py:470)
get_protocol_specification_id_from_specification  # unused function  (aea/helpers/protocols.py:60)
SERVICES  # unused variable (aea/configurations/constants.py:57)
DEFAULT_SERVICE_CONFIG_FILE  # unused variable (aea/configurations/constants.py:65)
