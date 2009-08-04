# OpProtoc
from opprotoc.proto import Proto, Quantifier, Field, Message, Request, Event, Service

client_info = Message("ClientInfo",
                      fields=[Field(Proto.String, "format", 1),
                              Field(Proto.String, "uuid", 2)
                             ])

connection_info = Message("ConnectionInfo",
                          fields=[Field(Proto.Uint32,  "clientID",  1)
                                 ])

service = Message("Service",
                  fields=[Field(Proto.String, "name",          1)
                         ,Field(Proto.String, "version",       2)
                         ,Field(Proto.Uint32, "activeClients", 3)
                         ,Field(Proto.Uint32, "maxClients",    4)
                         ])

command = Message("CommandInfo",
                  fields=[Field(Proto.String, "name",       1)
                         ,Field(Proto.Uint32, "number",     2)
                         ,Field(Proto.Uint32, "messageID",  3)
                         ,Field(Proto.Uint32, "responseID", 4)
                         ])

event = Message("EventInfo",
                fields=[Field(Proto.String, "name",      1)
                       ,Field(Proto.Uint32, "number",    2)
                       ,Field(Proto.Uint32, "messageID", 3)
                       ])

service_info = Message("ServiceInfo",
                       fields=[Field(Proto.Message, "commandList", 1, message=command, q=Quantifier.Repeated)
                              ,Field(Proto.Message, "eventList",   2, message=event, q=Quantifier.Repeated)
                              ])

service_selection = Message("ServiceSelection",
                            fields=[Field(Proto.String, "name", 1)
                                   ])

field_info = Message("FieldInfo",
                     fields=[Field(Proto.String, "name",       1)
                            ,Field(Proto.Uint32, "type",       2) # double=1, float=2, int32=3, uint32=4, sint32=5, fixed32=6, sfixed32=7, bool=8, string=9, bytes=10, message=11, int64=12, uint64=13, sint64=14, fixed64=15, sfixed64=16
                            ,Field(Proto.Uint32, "number",     3)
                            ,Field(Proto.Uint32, "quantifier", 4, q=Quantifier.Optional, default=0) # required=0, optional=1, repeated=2
                            ,Field(Proto.Uint32, "messageID",  5, q=Quantifier.Optional)
                            ])

message_info = Message("MessageInfo",
                       fields=[Field(Proto.String,  "name",      1)
                              ,Field(Proto.Message, "fields",    2, q=Quantifier.Repeated, message=field_info)
                              ,Field(Proto.Uint32,  "parentID",  3)
                              ])

message_selection = Message("MessageSelection",
                            fields=[Field(Proto.String, "serviceName", 1)
                                   ,Field(Proto.Uint32, "id",          2, q=Quantifier.Repeated)
                                   ])

service_result = Message("ServiceResult",
                         fields=[Field(Proto.String, "name", 1)
                                ])

host_info = Message("HostInfo",
                      fields=[Field(Proto.Uint32,  "stpVersion",      1)
                             ,Field(Proto.String,  "coreVersion",     2)
                             ,Field(Proto.String,  "platform",        3)
                             ,Field(Proto.String,  "operatingSystem", 4)
                             ,Field(Proto.String,  "userAgent",       5)
                             ,Field(Proto.Message, "serviceList",     6, message=service, q=Quantifier.Repeated)
                             ])

client_id = Message("ClientID",
                    fields=[Field(Proto.String, "uuid", 1)
                           ])

service_list = Message("ServiceList",
                       fields=[Field(Proto.String, "serviceList",    1, q=Quantifier.Repeated)
                              ])

error_info = Message("ErrorInfo",
                     fields=[Field(Proto.String, "description", 1)
                            ])

window_manager = Service("Scope", version="1.0", coreRelease="2.4",
                         commands=[Request(3, "Connect",    client_info,       connection_info)
                                  ,Request(4, "Disconnect", client_id,         False)
                                  ,Request(5, "Enable",     service_selection, service_result)
                                  ,Request(6, "Disable",    service_selection, service_result)
                                  ,Request(7, "Info",       service_selection, service_info)
                                  ,Request(8, "Quit",       False,             False)
                                  ,Request(10, "HostInfo",  False,             host_info)
                                  ,Request(11, "MessageInfo", message_selection, message_info)
                                  ,Event(0, "OnServices",       service_list)
                                  ,Event(1, "OnQuit",           False)
                                  ,Event(2, "OnConnectionLost", False)
                                  ,Event(9, "OnError",          error_info)
                                  ],
                         cpp_class="OpScopeProtocolService", cpp_hfile="modules/scope/src/scope_protocol_service.h")
