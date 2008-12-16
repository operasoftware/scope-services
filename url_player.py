# OpProtoc
from opprotoc.proto import Proto, Quantifier, Field, Message, Request, Event, Service

# Service: UrlPlayer
# TODO: This service should probable be replaced with the Exec service.

urlplayer_window = Message("WindowData",
                           fields=[Field(Proto.Uint32, "windowCount", 1)
                                  ])

urlplayer_window_info = Message("WindowInfo",
                                fields=[Field(Proto.Uint32, "windowCount", 1)
                                       ])

urlplayer_play = Message("PlayUrl",
                         fields=[Field(Proto.Uint32, "windowNumber", 1)
                                ,Field(Proto.String, "url",          2)
                                ])

url_player = Service("UrlPlayer",
                     commands=[Request(1,  "CreateWindows", urlplayer_window, urlplayer_window_info)
                              ,Request(3,  "LoadUrl",       urlplayer_play,   False)
                              ],
                     cpp_class="OpScopeUrlPlayer", cpp_hfile="modules/scope/src/urlplayer_command.h")
