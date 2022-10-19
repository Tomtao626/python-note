var get_sign;
navigator={}
navigator.userAgent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36";
window=global;
location={};
location.protocol={};
var kk;
!function(n) {
    var i = {};
    function o(e) {
        if (i[e])
            return i[e].exports;
        var t = i[e] = {
            "i": e,
            "l": !1,
            "exports": {}
        };
        return n[e].call(t.exports, t, t.exports, o),
        t.l = !0,
        t.exports
    }
    o.m = n,
    o.c = i,
    o.d = function(e, t, n) {
        o.o(e, t) || Object.defineProperty(e, t, {
            "enumerable": !0,
            "get": n
        })
    }
    ,
    o.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            "value": "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            "value": !0
        })
    }
    ,
    o.t = function(t, e) {
        if (1 & e && (t = o(t)),
        8 & e)
            return t;
        if (4 & e && "object" == typeof t && t && t.__esModule)
            return t;
        var n = Object.create(null);
        if (o.r(n),
        Object.defineProperty(n, "default", {
            "enumerable": !0,
            "value": t
        }),
        2 & e && "string" != typeof t)
            for (var i in t)
                o.d(n, i, function(e) {
                    return t[e]
                }
                .bind(null, i));
        return n
    }
    ,
    o.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e["default"]
        }
        : function() {
            return e
        }
        ;
        return o.d(t, "a", t),
        t
    }
    ,
    o.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    o.p = "",
    o(o.s = 28)
    get_sign=o;
}([function(e, t, o) {
    t = function(e, t, n) {
        o(29);
        var i = {};
        i.Class = o(11),
        i.cookie = {},
        i.cookie.get = o(31),
        i.cookie.set = o(33),
        i.cookie.remove = o(34),
        i.browser = o(14),
        i.floater = o(35),
        i.floaterView = o(36),
        i.logServer = o(39),
        i.page = {},
        i.page.getViewWidth = o(21),
        i.page.getViewHeight = o(20),
        i.page.getScrollLeft = o(22),
        i.page.getScrollTop = o(23),
        i.page.getWidth = o(40),
        i.page.getHeight = o(41),
        i.md5 = o(42),
        i.extend = o(43),
        i.load = o(44),
        i.rsaUtils = o(45),
        n.exports = i
    }
    .call(t, o, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        var s = function(e, t) {
            var n, i;
            if ("function" == typeof t)
                for (n in e)
                    if (e.hasOwnProperty(n) && (i = e[n],
                    !1 === t.call(e, i, n)))
                        break;
            return e
        }
          , a = function(e) {
            return "[object Array]" === Object.prototype.toString.call(e)
        }
          , i = function(e, t) {
            var n, i = [], o = t || function(e) {
                return String(e).replace(/[#%&+=\/\\\ \u3000\f\r\n\t]/g, function(e) {
                    return "%" + (256 + e.charCodeAt()).toString(16).substring(1).toUpperCase()
                })
            }
            ;
            return s(e, function(e, t) {
                if (a(e))
                    for (n = e.length; n--; )
                        i.push(t + "=" + o(e[n], t));
                else
                    i.push(t + "=" + o(e, t))
            }),
            i.join("&")
        }
          , o = {}
          , r = function(e, n, i) {
            e && (e.removeEventListener ? e.removeEventListener(n, i, !1) : e.attachEvent && e.detachEvent("on" + n, i),
            o[n].forEach(function(e, t) {
                e.eventHandle == i && o[n].splice(t, 1)
            }))
        };
        n.exports = {
            "getElementByAttr": function(e, t, n) {
                for (var i = ("undefined" == typeof arguments[3] ? document : arguments[3]).getElementsByTagName(e), o = [], s = 0; s < i.length; s++)
                    i[s].getAttribute(t) == n && o.push(i[s]);
                return o
            },
            "isEmptyObject": function(e) {
                for (var t in e)
                    return !1;
                return !0
            },
            "removeAllChild": function(e) {
                if (e && e.hasChildNodes())
                    for (var t = e.childNodes(), n = t.length - 1; 0 <= n; n--)
                        e.removeChild(t[n])
            },
            "on": function(e, t, n) {
                t = t,
                n = n,
                (e = e) && (o[t] = o[t] || [],
                o[t].push({
                    "type": t,
                    "elem": e,
                    "eventHandle": n
                }),
                e.addEventListener ? e.addEventListener(t, n, !1) : e.attachEvent && e.attachEvent("on" + t, n))
            },
            "un": function(e, t, n) {
                r(e, t, n)
            },
            "unAll": function(e) {
                !function() {
                    for (var e in o)
                        o[e].forEach(function(e) {
                            r(e.elem, e.type, e.eventHandle)
                        });
                    o = {}
                }()
            },
            "getQueryValue": function(e, t) {
                if (e) {
                    t = new RegExp("(^|&|\\?|#)" + String(t).replace(new RegExp("([.*+?^=!:${}()|[\\]/\\\\])","g"), "\\$1") + "=([^&#]*)(&|$|#)",""),
                    t = e.match(t);
                    return t ? t[2] : ""
                }
                return ""
            },
            "forEach": s,
            "isArray": a,
            "jsonToQuery": i,
            "isCors": function() {
                var e = !1;
                return e = window.XMLHttpRequest && "withCredentials"in new window.XMLHttpRequest ? !0 : e
            }
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(t, n, r) {
    (function(a) {
        var e = function(e, t, n) {
            var i = r(15).getDomain()
              , o = {
                "agenttype": "1",
                "ptid": "01010021010000000000",
                "protocolDom": "",
                "logoUrl": "",
                "msg": "请稍后重试",
                "fromSDK": "1",
                "sdk_version": "1.0.0",
                "domain": i = "iqiyi.com" != i && "pps.tv" != i && "beatshome.com" != i ? "iqiyi.com" : i,
                "globalEvent": "login,logout,pcloginsdkshow,pcloginsdkhide"
            }
              , s = {};
            n.exports = {
                "initConfig": function(e) {
                    s = a.extend(s, o),
                    s = a.extend(s, e)
                },
                "getConfig": function() {
                    return s
                }
            }
        }
        .call(n, r, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, r(0))
}
, function(e, t, n) {
    t = function(e, t, n) {
        var i = function(e, t) {
            var n = [];
            return e && e.className && (n = e.className.split(" ")),
            !!((t = String(t || "").trim()) && 0 <= n.indexOf(t))
        };
        n.exports = {
            "hasClass": i,
            "addClass": function(e, t) {
                var n;
                e && (t = String(t || "").trim(),
                n = e.className,
                t && !i(e, t) && (n = n + " " + t),
                e.className = n)
            },
            "removeClass": function(e, t) {
                if (e) {
                    var n = e.className && e.className.split(" ") || ""
                      , i = n && n.length || 0;
                    if (i) {
                        t = String(t).trim();
                        for (var o = 0; o < i; o++)
                            if (t == n[o]) {
                                n.splice(o, 1);
                                break
                            }
                        e.className = n.join(" ")
                    }
                }
            }
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        var o = window.PCLoginSDK && window.PCLoginSDK.eventList || {};
        n.exports = {
            "on": function(e, t) {
                t = t,
                e = (e = (e = e).replace(/^on/i, "")).toLowerCase(),
                o[e] = o[e] || [],
                o[e].push({
                    "type": e,
                    "listener": t
                }),
                window.PCLoginSDK.eventList = o
            },
            "un": function(e, t) {
                !function(e, n) {
                    e = e.replace(/^on/i, "").toLowerCase();
                    var t, i = o[e];
                    i && (i.length,
                    t = !n,
                    i && 0 < i.length && (1 == t ? o[e] = [] : i.forEach(function(e, t) {
                        e.listener === n && i.splice(t, 1)
                    })))
                }(e, t)
            },
            "unAll": function(e) {
                !function(n) {
                    for (var e in o)
                        o[e].forEach(function(e) {
                            var t = new RegExp("(^|,)" + e.type + "(,|$)");
                            n.search(t) < 0 && (o[e.type] = [])
                        })
                }(e)
            },
            "fire": function(e) {
                var n, i;
                n = (e = e).type.replace(/^on/i, "").toLowerCase(),
                i = e.data,
                (e = o[n]) && 0 < e.length && e.forEach(function(e) {
                    try {
                        e.listener({
                            "type": n,
                            "data": i
                        })
                    } catch (t) {}
                })
            }
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, o) {
    t = function(e, t, n) {
        var i = o(15).getDomain()
          , i = {
            "logout": "https://passport." + i + "/apis/user/logout.action",
            "thirdLogin": "https://passport." + i + "/apis/thirdparty/nlogin.action",
            "delcookiePPS": "https://passport.pps.tv/apis/user/delcookie.action",
            "delcookieIQIYI": "https://passport.iqiyi.com/apis/user/delcookie.action",
            "ssoTokenPPS": "https://passport.pps.tv/apis/user/sso/cd/token.action",
            "ssoCookieIQIYI": "https://passport.iqiyi.com/apis/user/sso/cd/cookie.action",
            "ssoTokenIQIYI": "https://passport.iqiyi.com/apis/user/sso/cd/token.action",
            "ssoCookiePPS": "https://passport.pps.tv/apis/user/sso/cd/cookie.action",
            "genLoginToken": "https://passport." + i + "/apis/qrcode/gen_login_token.action",
            "isTokenLogin": "https://passport." + i + "/apis/qrcode/is_token_login.action",
            "getAreacode": "https://passport." + i + "/apis/phone/get_support_areacode.action",
            "login": "https://passport." + i + "/apis/reglogin/login.action",
            "secureSendCode": "https://passport." + i + "/apis/phone/secure_send_cellphone_authcode.action",
            "authcodeLogin": "https://passport." + i + "/apis/reglogin/authcode_login.action",
            "upBizInfo": "https://passport." + i + "/apis/phone/up_biz_info.action",
            "upBizStatus": "https://passport." + i + "/apis/phone/up_biz_status.action",
            "validate": "https://passport." + i + "/apis/phone/verify_cellphone_authcode.action",
            "checkAccount": "https://passport." + i + "/apis/user/check_account.action",
            "userRegConfirm": "https://passport." + i + "/apis/reglogin/user_reg_confirm.action",
            "directBindPhone": "https://passport." + i + "/apis/phone/direct_bind_phone.action",
            "verifyAccount": "https://passport." + i + "/apis/phone/verify_account.action",
            "bindLogin": "https://passport." + i + "/apis/reglogin/bind_login.action"
        };
        n.exports = i
    }
    .call(t, o, t, e);
    t === undefined || (e.exports = t)
}
, function(t, n, r) {
    (function(a) {
        var e = function(e, t, n) {
            var i = r(12)
              , o = r(3)
              , s = r(8);
            n.exports = a.Class("Adapter", {
                "construct": function(e) {
                    this._options = e || {}
                },
                "methods": {
                    "init": function() {},
                    "render": function() {},
                    "renderHtml": function(e, t) {
                        return i.compile(e)(t)
                    },
                    "bindEvent": function() {},
                    "show": function(e) {
                        o.removeClass(e, "dn"),
                        this.rpage && (e = {
                            "rpage": this.rpage
                        },
                        this.block ? (e.block = this.block,
                        s.block(e)) : s.show(e))
                    },
                    "hide": function(e) {
                        o.addClass(e, "dn")
                    },
                    "destroy": function() {}
                }
            })
        }
        .call(n, r, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, r(0))
}
, function(t, n, o) {
    (function(p) {
        var e = function(e, t, n) {
            var a = o(50)
              , r = o(51)
              , c = o(1)
              , d = o(2)
              , l = o(13)
              , u = o(9)
              , i = p.Class("RemoteInterface", {
                "construct": function(e) {
                    this._remoteInterfaces = e
                },
                "statics": {
                    "protocol": c.isCors() ? "https:" : window.location.protocol
                },
                "methods": {
                    "send": function(i, o) {
                        var e = !1 !== i.withCredentials
                          , t = i.ifname
                          , s = this._getIfData(t);
                        c.isCors() ? r.request(s.url, {
                            "data": i.param,
                            "method": "POST",
                            "withCredentials": e,
                            "onsuccess": function(e) {
                                o && o(e)
                            },
                            "onerror": function(e) {
                                o && o({
                                    "code": "E00000",
                                    "msg": "系统异常，请稍后重试"
                                }),
                                window.MITO && window.MITO.log({
                                    "message": s.url + "接口调用失败(高版本浏览器)",
                                    "data": i.param
                                })
                            },
                            "onfailure": function(e) {
                                var t = d.getConfig()
                                  , n = t.appVersion;
                                "pca" == t.business && l.isUpgrade(n, "8.9.142.1") ? u.callPca() : o && o({
                                    "code": "A00101",
                                    "msg": "系统异常，请稍后重试"
                                }),
                                window.MITO && window.MITO.log({
                                    "message": s.url + "接口调用超时",
                                    "data": i.param
                                })
                            }
                        }) : (e = {
                            "__POST": 1,
                            "cb": 1
                        },
                        e = p.extend(e, i.param),
                        new a({
                            "form": {
                                "action": s.url
                            },
                            "data": e,
                            "callback": o,
                            "needDestroy": !0,
                            "needMd5": i.needMd5
                        }).submit())
                    },
                    "_getIfData": function(e) {
                        return this._remoteInterfaces[e] || this._remoteInterfaces
                    },
                    "_getUrl": function(e, t) {
                        var n, i = [];
                        for (n in t)
                            i.push(n + "=" + t[n]);
                        return e + "?" + i.join("&")
                    }
                }
            });
            n.exports = i
        }
        .call(n, o, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, o(0))
}
, function(t, n, s) {
    (function(o) {
        var e = function(e, t, n) {
            var i = s(2);
            n.exports = {
                "show": function(e) {
                    e = this.getParam("22", e),
                    o.logServer(e)
                },
                "block": function(e) {
                    e = this.getParam("21", e),
                    o.logServer(e)
                },
                "click": function(e) {
                    e = this.getParam("20", e),
                    o.logServer(e)
                },
                "getParam": function(e, t) {
                    var n = i.getConfig()
                      , e = {
                        "p1": "1_10_101",
                        "pu": o.cookie.get("P00003"),
                        "stime": (new Date).getTime(),
                        "u": n.deviceid || o.cookie.get("QC005") || "",
                        "bstp": "56",
                        "t": e
                    };
                    return n.pingback && (e = o.extend(e, n.pingback)),
                    e = o.extend(e, t)
                }
            }
        }
        .call(n, s, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, s(0))
}
, function(e, t, i) {
    t = function(e, t, n) {
        var o = i(12)
          , s = i(3)
          , a = i(1)
          , r = i(52);
        n.exports = {
            "loginSuc": function(e, t) {
                t = o.compile(r)({
                    "type": "suc",
                    "icon": t.icon,
                    "nickname": t.nickname,
                    "tip": t.tip,
                    "title": t.title
                });
                e.innerHTML = t,
                s.removeClass(e, "dn")
            },
            "showTip": function(t, e) {
                e = o.compile(r)({
                    "type": "tip",
                    "tip": e.tip,
                    "btnTip": e.btnTip
                });
                t.innerHTML = e,
                s.removeClass(t, "dn");
                var n = t.querySelector('[data-toast="btn"]')
                  , i = function(e) {
                    e.stopPropagation && e.stopPropagation(),
                    a.un(n, "click", i),
                    s.addClass(t, "dn")
                };
                a.on(n, "click", i)
            },
            "showMsg": function(e, t) {
                var n = o.compile(r)({
                    "type": "toast",
                    "tip": t.tip
                })
                  , t = t.time || 1800;
                e.innerHTML = n,
                s.removeClass(e, "dn"),
                setTimeout(function() {
                    s.addClass(e, "dn")
                }, t)
            },
            "callPca": function() {
                var t = document.querySelector('[data-login-sdk="panel"]').querySelector('[data-login-sdk="toast"]')
                  , e = o.compile(r)({
                    "type": "tip",
                    "tip": "非常抱歉，页面加载出错~",
                    "btnTip": "重试"
                });
                t.innerHTML = e,
                s.removeClass(t, "dn");
                var n = t.querySelector('[data-toast="btn"]')
                  , i = function(e) {
                    e.stopPropagation && e.stopPropagation(),
                    a.un(n, "click", i);
                    window.external.js_app_service('{"call_type":"request", "cmd":"switch_pca_login", "cmd_context":"", "cmd_data":{}}'),
                    setTimeout(function() {
                        s.addClass(t, "dn")
                    }, 100)
                };
                a.on(n, "click", i)
            }
        }
    }
    .call(t, i, t, e);
    t === undefined || (e.exports = t)
}
, function(t, n, h) {
    (function(p) {
        var e = function(e, t, n) {
            var i, o, s = h(2), a = [], r = null, c = !1, d = null, l = function(t) {
                r ? r && r.tryGetFingerPrint ? t(r.tryGetFingerPrint() || "") : r.getFingerPrint ? r.getFingerPrint(function(e) {
                    t(e)
                }, function(e) {
                    t("")
                }) : t("") : t("")
            };
            function u() {
                if (r = window.dfp,
                0 < a.length)
                    for (; 0 < a.length; )
                        try {
                            var e = a.shift();
                            l(e.cb)
                        } catch (t) {}
                else
                    r && (r && r.tryGetFingerPrint ? r.tryGetFingerPrint() : r.getFingerPrint && r.getFingerPrint(function() {}))
            }
            window.dfp && (window.dfp.tryGetFingerPrint || window.dfp.getFingerPrint) ? u() : (o = document.getElementsByTagName("HEAD").item(0),
            (i = document.createElement("script")).type = "text/javascript",
            i.src = "//security.iqiyi.com/static/cook/v1/cooksdk.js",
            p.browser.iPad && (i.src = "//security.iqiyi.com/static/cook/v1/cooksdkpcwpad.js"),
            o.appendChild(i),
            o = navigator.userAgent.toLowerCase(),
            /msie/.test(o) ? i.onreadystatechange = function() {
                /loaded|complete/.test(i.readyState) && (c = !0,
                clearTimeout(d),
                u())
            }
            : i.onload = function() {
                c = !0,
                clearTimeout(d),
                u()
            }
            ),
            n.exports = {
                "getDFP": function(e) {
                    var t = s.getConfig();
                    t.dfp ? e(t.dfp) : r ? l(e) : (a.push({
                        "cb": e
                    }),
                    clearTimeout(d),
                    d = setTimeout(function() {
                        c || (clearTimeout(d),
                        u())
                    }, 2e3))
                }
            }
        }
        .call(n, h, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, h(0))
}
, function(e, t, i) {
    t = function(e, t, n) {
        var m = i(30);
        n.exports = function(e, t) {
            var r = t.ns && t.ns + "." + e;
            if (r)
                try {
                    var n = new Function("return " + r)();
                    if (n)
                        return n
                } catch (f) {}
            var i = t.extend || m
              , o = function() {}
              , s = t.plugins || [];
            o.prototype = i.prototype;
            var a = t.construct || function() {}
              , c = t.properties || {}
              , d = t.methods || {}
              , l = t.statics || {}
              , u = new o;
            for (h in u)
                u.hasOwnProperty(h) && delete u[h];
            for (h in c)
                u[h] = c[h];
            for (h in d)
                u[h] = d[h];
            for (var p = 0; p < s.length; p++) {
                var h, g = s[p];
                for (h in g)
                    u[h] = g[h]
            }
            for (h in u.constructor = a,
            u.superclass = i,
            u.superinstance = new o,
            u.__NAME__ = e,
            a.prototype = u,
            l)
                a[h] = l[h];
            return r && function(e, t) {
                var n, i = r.split("."), o = i.length - 1, s = 0;
                if (!t)
                    try {
                        if (!new RegExp("^[a-zA-Z_$][a-zA-Z0-9_$]*$").test(i[0]))
                            throw "";
                        t = new Function("return " + i[0])(),
                        s = 1
                    } catch (a) {
                        t = window
                    }
                for (; s < o; s++)
                    t[n = i[s]] || (t[n] = {}),
                    t = t[n];
                t[i[o]] || (t[i[o]] = e)
            }(a),
            a
        }
    }
    .call(t, i, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        var x, s;
        !function(i) {
            "use strict";
            (x = function(e, t) {
                return x["string" == typeof t ? "compile" : "render"].apply(x, arguments)
            }
            ).version = "2.0.2",
            x.openTag = "<%",
            x.closeTag = "%>",
            x.isEscape = !0,
            x.isCompress = !1,
            x.parser = null,
            x.render = function(e, t) {
                return (x.get(e) || d({
                    "id": e,
                    "name": "Render Error",
                    "message": "No Template"
                }))(t)
            }
            ,
            x.compile = function(t, n) {
                var i, e = arguments, o = e[2], s = "anonymous";
                "string" != typeof n && (o = e[1],
                n = e[0],
                t = s);
                try {
                    i = l(t, n, o)
                } catch (r) {
                    return r.id = t || n,
                    r.name = "Syntax Error",
                    d(r)
                }
                function a(e) {
                    try {
                        return new i(e,t) + ""
                    } catch (r) {
                        return o ? d(r)() : x.compile(t, n, !0)(e)
                    }
                }
                return a.prototype = i.prototype,
                a.toString = function() {
                    return i.toString()
                }
                ,
                t !== s && (c[t] = a),
                a
            }
            ;
            var c = x.cache = {}
              , w = x.helpers = {
                "$include": x.render,
                "$string": function(e, t) {
                    return "string" != typeof e && ("number" == (t = typeof e) ? e += "" : e = "function" == t ? w.$string(e()) : ""),
                    e
                },
                "$escape": function(e) {
                    var t = {
                        "<": "&#60;",
                        ">": "&#62;",
                        '"': "&#34;",
                        "'": "&#39;",
                        "&": "&#38;"
                    };
                    return w.$string(e).replace(/&(?![\w#]+;)|[<>"']/g, function(e) {
                        return t[e]
                    })
                },
                "$each": function(e, t) {
                    if ((Array.isArray || function(e) {
                        return "[object Array]" === {}.toString.call(e)
                    }
                    )(e))
                        for (var n = 0, i = e.length; n < i; n++)
                            t.call(e, e[n], n, e);
                    else
                        for (var o in e)
                            t.call(e, e[o], o)
                }
            };
            x.helper = function(e, t) {
                w[e] = t
            }
            ,
            x.onerror = function(e) {
                var t, n = "Template Error\n\n";
                for (t in e)
                    n += "<" + t + ">\n" + e[t] + "\n\n";
                try {
                    window.MITO && window.MITO.log({
                        "message": "渲染出错了",
                        "data": {
                            "msg": n
                        }
                    })
                } catch (e) {}
            }
            ,
            x.get = function(e) {
                var t, n;
                return c.hasOwnProperty(e) ? n = c[e] : "document"in i && ((t = document.getElementById(e)) && (t = t.value || t.innerHTML,
                n = x.compile(e, t.replace(/^\s*|\s*$/g, "")))),
                n
            }
            ;
            var k, C, P, _, S, L, d = function(e) {
                return x.onerror(e),
                function() {
                    return "{Template Error}"
                }
            }, l = (k = w.$each,
            C = new RegExp(["\\/\\*[\\w\\W]*?\\*\\/", "\\/\\/[^\\n]*\\n", "\\/\\/[^\\n]*$", '"(?:[^"\\\\]|\\\\[\\w\\W])*"', "'(?:[^'\\\\]|\\\\[\\w\\W])*'", "[\\s\\t\\n]*\\.[\\s\\t\\n]*[$\\w\\.]+"].join("|"),"g"),
            P = /[^\w$]+/g,
            _ = new RegExp(["\\b" + "break,case,catch,continue,debugger,default,delete,do,else,false,finally,for,function,if,in,instanceof,new,null,return,switch,this,throw,true,try,typeof,var,void,while,with,abstract,boolean,byte,char,class,const,double,enum,export,extends,final,float,goto,implements,import,int,interface,long,native,package,private,protected,public,short,static,super,synchronized,throws,transient,volatile,arguments,let,yield,undefined".replace(/,/g, "\\b|\\b") + "\\b"].join("|"),"g"),
            S = /^\d[^,]*|,\d[^,]*/g,
            L = /^,+|,+$/g,
            function(e, t, o) {
                var n = x.openTag
                  , s = x.closeTag
                  , a = x.parser
                  , i = t
                  , r = ""
                  , c = 1
                  , d = {
                    "$data": 1,
                    "$id": 1,
                    "$helpers": 1,
                    "$out": 1,
                    "$line": 1
                }
                  , l = {}
                  , u = "var $helpers=this," + (o ? "$line=0," : "")
                  , p = "".trim
                  , h = p ? ["$out='';", "$out+=", ";", "$out"] : ["$out=[];", "$out.push(", ");", "$out.join('')"]
                  , p = p ? "if(content!==undefined){$out+=content;return content;}" : "$out.push(content);"
                  , g = "function(content){" + p + "}"
                  , f = "function(id,data){data=data||$data;var content=$helpers.$include(id,data,$id);" + p + "}";
                function m(e) {
                    return "'" + e.replace(/('|\\)/g, "\\$1").replace(/\r/g, "\\r").replace(/\n/g, "\\n") + "'"
                }
                k(i.split(n), function(e, t) {
                    var n = (e = e.split(s))[0]
                      , i = e[1];
                    1 === e.length ? r += y(n) : (r += function(e) {
                        var t = c;
                        a ? e = a(e) : o && (e = e.replace(/\n/g, function() {
                            return "$line=" + ++c + ";"
                        }));
                        {
                            var n;
                            0 === e.indexOf("=") && (n = 0 !== e.indexOf("=="),
                            e = e.replace(/^=*|[\s;]*$/g, ""),
                            n && x.isEscape ? (n = e.replace(/\s*\([^\)]+\)/, ""),
                            w.hasOwnProperty(n) || /^(include|print)$/.test(n) || (e = "$escape(" + e + ")")) : e = "$string(" + e + ")",
                            e = h[1] + e + h[2])
                        }
                        o && (e = "$line=" + t + ";" + e);
                        return function(e) {
                            e = function(e) {
                                var e = e.replace(C, "").replace(P, ",").replace(_, "").replace(S, "").replace(L, "").split(",")
                                  , t = [];
                                return k(e, function(e) {
                                    "" != e && t.push(e)
                                }),
                                t
                            }(e),
                            k(e, function(e) {
                                var t, n;
                                d.hasOwnProperty(e) || ("print" === (t = e) ? n = g : "include" === t ? (l["$include"] = w["$include"],
                                n = f) : (n = "$data." + t,
                                w.hasOwnProperty(t) && (l[t] = w[t],
                                n = 0 === t.indexOf("$") ? "$helpers." + t : n + "===undefined?$helpers." + t + ":" + n)),
                                u += t + "=" + n + ",",
                                d[e] = !0)
                            })
                        }(e),
                        e + "\n"
                    }(n),
                    i && (r += y(i)))
                }),
                i = r,
                o && (i = "try{" + i + "}catch(e){throw {id:$id,name:'Render Error',message:e.message,line:$line,source:" + m(t) + ".split(/\\n/)[$line-1].replace(/^[\\s\\t]+/,'')};}"),
                i = u + h[0] + i + "return new String(" + h[3] + ");";
                try {
                    var v = new Function("$data","$id",i);
                    return v.prototype = l,
                    v
                } catch (b) {
                    throw b.temp = "function anonymous($data,$id) {" + i + "}",
                    b
                }
                function y(e) {
                    return c += e.split(/\n/).length - 1,
                    e = (e = x.isCompress ? e.replace(/[\n\r\t\s]+/g, " ").replace(/<!--.*?-->/g, "") : e) && h[1] + m(e) + h[2] + "\n"
                }
            }
            )
        }(window),
        (s = x).openTag = "{{",
        s.closeTag = "}}",
        s.parser = function(e) {
            var t = (e = e.replace(/^\s/, "")).split(" ")
              , n = t.shift()
              , i = t.join(" ");
            switch (n) {
            case "if":
                e = "if(" + i + "){";
                break;
            case "else":
                e = "}else" + (t = "if" === t.shift() ? " if(" + t.join(" ") + ")" : "") + "{";
                break;
            case "/if":
                e = "}";
                break;
            case "each":
                var o = t[0] || "$data";
                e = "$each(" + (o = "as" !== (t[1] || "as") ? "[]" : o) + ",function(" + ((t[2] || "$value") + "," + (t[3] || "$index")) + "){";
                break;
            case "/each":
                e = "});";
                break;
            case "echo":
                e = "print(" + i + ");";
                break;
            case "include":
                e = "include(" + t.join(",") + ");";
                break;
            default:
                e = s.helpers.hasOwnProperty(n) ? "==" + n + "(" + t.join(",") + ");" : "=" + (e = e.replace(/[\s;]*$/, ""))
            }
            return e
        }
        ,
        n.exports = x
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        var i = {
            "mail": function(e) {
                e = e.replace(/(^\s*)|(\s*$)/g, "");
                return /^[0-9a-zA-Z_][-_\.0-9a-zA-Z-]{1,}@([0-9a-zA-Z][0-9a-zA-Z-]*\.)+[a-zA-Z]{2,4}$/.test(e)
            },
            "mobile": function(e, t) {
                var n = "86" == t && /^(1\d{10})$/.test(e.trim())
                  , i = "886" == t && /^\d{10}$/gi.test(e.trim())
                  , e = "86" != t && "86" != t && 4 < e.trim().length && e.trim().length < 20;
                return n || i || e
            },
            "trimSE": function(e) {
                return e.replace(/(^\s*)|(\s*$)/g, "")
            },
            "number": function(e) {
                return /^\d+(\.\d+)?$/.test(e)
            },
            "trimAllBlank": function(e) {
                return e.replace(/\s/g, "")
            },
            "isUpgrade": function(e, t) {
                if (!e)
                    return !1;
                for (var n = t.split("."), i = e.split("."), o = !0, s = 0; s < n.length; s++) {
                    if (parseInt(n[s]) < parseInt(i[s])) {
                        o = !0;
                        break
                    }
                    if (parseInt(n[s]) !== parseInt(i[s])) {
                        o = !1;
                        break
                    }
                }
                return o
            }
        };
        n.exports = i
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        var i = {}
          , o = navigator.userAgent.toLowerCase()
          , s = (navigator.plugins,
        o.match(/trident/))
          , a = !s && o.match(/(ipad).*os\s([\d_]+)/)
          , r = !s && !a && o.match(/(iphone\sos)\s([\d_]+)/)
          , c = o.match(/(Android)\s+([\d.]+)/);
        i.IE11 = /rv\:11/.test(o),
        i.IE = /msie/.test(o) || i.IE11,
        i.OPERA = /opera/.test(o),
        i.MOZ = /gecko/.test(o),
        i.IE8 = /msie 8/.test(o),
        i.IE9 = /msie 9/.test(o),
        i.IE10 = /msie 10/.test(o),
        i.EDGE = /edge/.test(o),
        i.SAFARI = /safari/.test(o) && !/chrome/.test(o),
        i.mobileSafari = (/iPhone/i.test(navigator.platform) || /iPod/i.test(navigator.platform) || /iPad/i.test(navigator.userAgent)) && !!navigator.appVersion.match(/(?:Version\/)([\w\._]+)/),
        i.WEBKIT = /webkit/.test(o),
        i.CHROME = /chrome/.test(o),
        i.iPhone = /iphone os/.test(o) && !s,
        i.iPod = /iPod/i.test(o) && !s,
        i.android = /android/.test(o),
        i.iPhone4 = /iphone os [45]_/.test(o) && !s,
        i.iPad = /ipad/.test(o) && !s,
        i.WP = /windows phone/.test(o),
        i.baidu = /baidu/.test(o),
        i.mbaidu = /baidu/.test(o),
        i.m360 = /360/.test(o),
        i.muc = /uc/.test(o),
        i.mqq = /qq/.test(o),
        c && (i.version = c[2]),
        r && (i.ios = !0,
        i.version = r[2].replace(/_/g, ".")),
        a && (i.ios = !0,
        i.version = a[2].replace(/_/g, ".")),
        i.iPod && (i.ios = !0),
        i.lePad = /lepad_hls/.test(o),
        i.Mac = /macintosh/.test(o),
        i.TT = /tencenttraveler/.test(o),
        i.$360 = /360se/.test(o),
        i.ff = /firefox/.test(o),
        i.uc = /uc/.test(o),
        i.Maxthon = !1;
        try {
            i.html5Video = !!document.createElement("video").play
        } catch (l) {
            i.html5Video = !1
        }
        try {
            var d = window.external;
            i.Maxthon = !!d.max_version
        } catch (l) {}
        n.exports = i
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}

, function(t, n, o) {
    (function(i) {
        var e = function(e, t, n) {
            n.exports = {
               "rsaFun": function(e) {
                    var t = i.rsaUtils.getKeyPair("10001", "", "ab86b6371b5318aaa1d3c9e612a9f1264f372323c8c0f19875b5fc3b3fd3afcc1e5bec527aa94bfa85bffc157e4245aebda05389a5357b75115ac94f074aefcd");
                    return i.rsaUtils.encryptedString(t, encodeURIComponent(e)).replace(/\s/g, "-")
                }

            }
        }
        .call(n, o, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, o(0))
}
, function(e, t, s) {
    t = function(e, t, n) {
        var i = s(3)
          , o = s(9);
        n.exports = {
            "isAgree": function(e) {
                var t = document.querySelector('[data-login-sdk="panel"]')
                  , n = t.querySelector('[data-login-sdk="toast"]')
                  , t = t.querySelector('[data-login-sdk="protocol"]').querySelector('[data-protocol-btn="agree"]');
                return !(t && !i.hasClass(t, "selected")) || (o.showMsg(n, {
                    "tip": e || "请阅读并勾选页面底部的协议"
                }),
                !1)
            }
        }
    }
    .call(t, s, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        n.exports = function(e) {
            return new RegExp('^[^\\x00-\\x20\\x7f\\(\\)<>@,;:\\\\\\"\\[\\]\\?=\\{\\}\\/\\u0080-\\uffff]+$').test(e)
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, i) {
    t = function(e, t, n) {
        var o = i(18);
        n.exports = function(e, t, n) {
            var i;
            o(e) && (i = (n = n || {}).expires,
            "number" == typeof n.expires && (i = new Date).setTime(i.getTime() + n.expires),
            document.cookie = e + "=" + t + (n.path ? "; path=" + n.path : "") + (i ? "; expires=" + i.toGMTString() : "") + (n.domain ? "; domain=" + n.domain : "") + (n.secure ? "; secure" : ""))
        }
    }
    .call(t, i, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        n.exports = function(e) {
            var t = document
              , t = "BackCompat" == t.compatMode ? t.body : t.documentElement;
            return window.innerHeight || t.clientHeight
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        n.exports = function(e) {
            var t = document
              , t = "BackCompat" == t.compatMode ? t.body : t.documentElement;
            return window.innerWidth || t.clientWidth
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        n.exports = function() {
            var e = window
              , t = e.document
              , n = t.documentElement;
            return e.pageXOffset || n && n.scrollLeft || t.body.scrollLeft
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        n.exports = function() {
            var e = window
              , t = e.document
              , n = t.documentElement;
            return e.pageYOffset || n && n.scrollTop || t.body.scrollTop
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(t, n, h) {
    (function(p) {
        var e = function(e, t, n) {
            var i = h(6)
              , o = h(12)
              , r = h(1)
              , c = h(3)
              , d = h(4)
              , a = new (h(49))
              , s = h(53)
              , l = [{
                "acode": "86",
                "name": "中国大陆",
                "selected": "selected"
            }, {
                "acode": "886",
                "name": "台湾",
                "selected": ""
            }]
              , u = [];
            n.exports = p.Class("areaListAction", {
                "extend": i,
                "construct": function(e) {
                    this.fireName = e.fireName,
                    this.panel = e.panel,
                    this.acode = l[0].acode,
                    this.name = l[0].name
                },
                "methods": {
                    "render": function() {
                        var t = this;
                        this.getAreaList(function(e) {
                            e = o.compile(s)({
                                "lists": e
                            });
                            t.panel.innerHTML = e,
                            t.bindEvent()
                        })
                    },
                    "getAreaList": function(o) {
                        var s = this;
                        0 < u.length ? o(u) : a.getAreacode(function(e) {
                            var t = ""
                              , n = "";
                            if ("A00000" == e.code && e.data)
                                for (var i in acode = e.data.acode,
                                e.data.local && (t = e.data.local.acode,
                                n = e.data.local.name),
                                acode)
                                    u.push({
                                        "acode": i,
                                        "name": acode[i],
                                        "selected": t == i ? "selected" : ""
                                    });
                            else
                                u = l,
                                window.MITO && window.MITO.log({
                                    "message": "区域列表接口get_support_areacode.action失败",
                                    "data": e
                                });
                            s.acode = t || s.acode,
                            s.name = n || s.name,
                            o(u)
                        })
                    },
                    "bindEvent": function() {
                        var n = this
                          , e = this.panel.querySelector('[data-area="panel"]')
                          , i = this.panel.querySelector('[data-area="listPanel"]')
                          , t = function(e) {
                            (e = e || window.event).stopPropagation && e.stopPropagation(),
                            c.removeClass(i, "dn")
                        };
                        r.on(e, "click", t);
                        for (var o = this.panel.querySelectorAll("[data-area-acode]"), s = function(e) {
                            (e = e || window.event).stopPropagation && e.stopPropagation();
                            var t = e.target || e.srcElement
                              , e = t.getAttribute("data-area-acode")
                              , t = t.getAttribute("data-area-name");
                            e != n.acode && (n.resetAcode(e, t),
                            d.fire({
                                "type": "globalAcodeChange",
                                "data": {
                                    "acode": e,
                                    "name": t
                                }
                            })),
                            c.addClass(i, "dn")
                        }, a = 0; a < o.length; a++)
                            r.on(o[a], "click", s);
                        r.on(i, "mouseover", t),
                        r.on(i, "mouseout", function(e) {
                            (e = e || window.event).stopPropagation && e.stopPropagation(),
                            c.addClass(i, "dn")
                        }),
                        p.browser.iPad && d.on("hideArea", function() {
                            c.addClass(i, "dn")
                        })
                    },
                    "getAcode": function() {
                        return {
                            "acode": this.acode,
                            "name": this.name
                        }
                    },
                    "resetAcode": function(e, t) {
                        var n, i;
                        e != this.acode && (n = this.panel.querySelector('[data-area="show"]'),
                        i = this.panel.querySelectorAll('[data-area-acode="' + e + '"]'),
                        c.removeClass(this.panel.querySelector('[data-area-acode="' + this.acode + '"]'), "selected"),
                        c.addClass(i, "selected"),
                        n.innerHTML = t + " +" + e,
                        this.acode = e,
                        this.name = t,
                        d.fire({
                            "type": this.fireName,
                            "data": e
                        }))
                    }
                }
            })
        }
        .call(n, h, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, h(0))
}
, function(t, n, s) {
    (function(o) {
        var e = function(e, t, n) {
            var i = s(1);
            n.exports = function(e, t) {
                return e = i.jsonToQuery(e),
                e = decodeURIComponent(e),
                o.md5(e + (t || "tS7BdPLU2w0JD89dh"))
            }
        }
        .call(n, s, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, s(0))
}
, function(t, n, p) {
    (function(u) {
        var e = function(e, t, n) {
            var i = p(3)
              , o = p(13)
              , s = p(4)
              , a = p(1)
              , r = "手机号格式错误，请重新输入"
              , c = "邮箱格式错误，请重新输入"
              , d = "系统异常，请重试"
              , l = function(e) {
                this.name = e.name,
                this.nameErr = e.nameErr,
                this.mailPanel = e.mailPanel,
                this.acode = e.acode || "86",
                this.fireEnableName = e.fireEnableName,
                this.zoneChangeFireName = e.zoneChangeFireName
            };
            l.prototype = {
                "init": function() {
                    this._bindEvent()
                },
                "_bindEvent": function() {
                    var t = this;
                    t._nameEvent(),
                    s.on(t.zoneChangeFireName, function(e) {
                        t.acode = e.data;
                        e = t.name.value.trim();
                        e && o.number(e) && (e = t.checkNameValidate(!0),
                        s.fire({
                            "type": t.fireEnableName,
                            "data": {
                                "enable": e
                            }
                        }))
                    })
                },
                "_nameEvent": function() {
                    var n = this;
                    a.on(n.name, "click", function(e) {
                        e.stopPropagation && e.stopPropagation(),
                        n.clearErrMsg()
                    }),
                    u.browser.iPad && a.on(n.name, "touchend", function(e) {
                        s.fire({
                            "type": "hideArea"
                        })
                    });
                    a.on(n.name, "blur", function(e) {
                        n.mailPanel && i.addClass(this.mailPanel, "dn");
                        var t = n.checkNameValidate(!0);
                        s.fire({
                            "type": n.fireEnableName,
                            "data": {
                                "enable": t
                            }
                        })
                    });
                    var e = function(e) {
                        e.stopPropagation && e.stopPropagation(),
                        n.clearErrMsg();
                        e = n.checkNameValidate();
                        s.fire({
                            "type": n.fireEnableName,
                            "data": {
                                "enable": e
                            }
                        })
                    };
                    a.on(n.name, "keyup", e),
                    a.on(n.name, "input", e)
                },
                "checkNameValidate": function(e) {
                    var t = this.name.value.trim();
                    return t ? o.number(t) ? this.checkMobileValidate(t, e) : this.mailPanel ? this.checkEmaiValidate(t, e) : e ? (this.showErrMsg(r),
                    !1) : void 0 : (this.name.value = "",
                    this.hideErrMsg(),
                    !1)
                },
                "checkMobileValidate": function(e, t) {
                    return o.mobile(e, this.acode) ? (this.hideErrMsg(),
                    !0) : t ? (this.showErrMsg(r),
                    !1) : void 0
                },
                "checkEmaiValidate": function(e, t) {
                    return 1 < e.indexOf("@") && o.mail(e) ? (this.hideErrMsg(),
                    !0) : t ? (this.showErrMsg(c),
                    !1) : void 0
                },
                "showErrMsg": function(e) {
                    this.nameErr.innerHTML = e || d,
                    i.removeClass(this.nameErr, "dn"),
                    i.addClass(this.namePlaceholder, "dn")
                },
                "hideErrMsg": function() {
                    i.addClass(this.nameErr, "dn")
                },
                "showPhoneMsg": function(e) {
                    this.showErrMsg(e || d)
                },
                "clearErrMsg": function() {
                    this.hideErrMsg()
                }
            },
            n.exports = l
        }
        .call(n, p, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, p(0))
}
, function(e, t, i) {
    t = function(e, t, n) {
        var p = i(1)
          , h = i(25)
          , g = function(e) {
            e.clearAttributes && e.clearAttributes(),
            e && e.parentNode && e.parentNode.removeChild(e),
            e = null
        };
        n.exports = function(e, t) {
            var n, i, o, s = t.data, a = t.timeout || 1e4, r = t.onsuccess, c = t.onfailure, d = "cb" + Math.floor(2147483648 * Math.random()).toString(36), l = "window.lib.__callbacks__." + d, u = window.lib.__callbacks__;
            r && (s["callback"] = l,
            t.sign && (s["qd_sc"] = h(s)),
            u[d] = function(e) {
                n && clearTimeout(n),
                r(e),
                delete u[d],
                g(i)
            }
            ,
            o = e + (o = e,
            RegExp("\\?").test(o) ? "&" : "?") + p.jsonToQuery(s, window.encodeURIComponent)),
            s = o,
            o = t.charset,
            (t = document.createElement("SCRIPT")).setAttribute("type", "text/javascript"),
            o && t.setAttribute("charset", o),
            t.setAttribute("src", s),
            document.getElementsByTagName("head")[0].appendChild(t),
            i = t,
            n = setTimeout(function() {
                g(i),
                c()
            }, a)
        }
    }
    .call(t, i, t, e);
    t === undefined || (e.exports = t)
}
, function(t, n, p) {
    (function(u) {
        var e = function(e, t, n) {
            var o = p(46)
              , i = p(4)
              , s = {
                "green": "//stc.iqiyipic.com/20210608/login-green.css",
                "pca": "//stc.iqiyipic.com/gaze/uniqy/main/js/qiyiLogin/20210608/login-green.css",
                "purple": "//stc.iqiyipic.com/20210524/login-purple.css",
                "red": "//stc.iqiyipic.com/20210524/login-red.css",
                "orange": "//stc.iqiyipic.com/20210524/login-dark-orange.css"
            }
              , a = null
              , r = {}
              , c = !1
              , d = function() {};
            function l(e, t, n) {
                var i;
                r = e || {},
                a = a || new o,
                t && !c ? (t = s[e.skin] || s.green,
                u.load("css", t, function() {
                    c = !0,
                    n()
                }),
                (e = e.cssUrl) && u.load("css", e, function() {}),
                "pca" == r.business || u.browser && (u.browser.IE8 || u.browser.IE9) || (i = function() {
                    MITO.init({
                        "platform": "b6c13e26323c537d",
                        "cid": 18,
                        "maxBreadcrumbs": 10,
                        "beforePushBreadcrumb": function(e, t) {
                            return "Console" !== t.type && t
                        },
                        "beforeDataReport": function(e) {
                            return (!e.message || !e.message.match(/(pan.iqiyi.com|datax.baidu.com|.jpg|.logo|qa.js|.png|sea1.2.js|msg.qy.net|pingBack|.gif)/)) && e
                        }
                    })
                }
                ,
                window.MITO ? i() : u.load("js", "https://stc.iqiyipic.com/js/common/mito.min.js", function() {
                    window.MITO && i()
                }))) : n()
            }
            d.openLoginRegWindow = function(e) {
                e && e.business && l(e, !0, function() {
                    a.openLoginRegWindow(r)
                })
            }
            ,
            d.logout = function(e) {
                l(e, !1, function() {
                    a.logout(r)
                })
            }
            ,
            d.isLogin = function() {
                return !!u.cookie.get("P00001")
            }
            ,
            d.on = function(e, t) {
                i.on(e, t)
            }
            ,
            d.un = function(e, t) {
                i.un(e, t)
            }
            ,
            window["PCLoginSDK"] = d
        }
        .call(n, p, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, p(0))
}
, function(e, t) {
    Function.prototype.bind || (Function.prototype.bind = function(e) {
        if ("function" != typeof this)
            throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable");
        var t = Array.prototype.slice.call(arguments, 1)
          , n = this
          , i = function() {}
          , o = function() {
            return n.apply(this instanceof i && e ? this : e, t.concat(Array.prototype.slice.call(arguments)))
        };
        return i.prototype = this.prototype,
        o.prototype = new i,
        o
    }
    ),
    String.prototype.trim = function() {
        return this.replace(/(^\s*)|(\s*$)/g, "")
    }
    ,
    "function" != typeof Array.prototype.forEach && (Array.prototype.forEach = function(e) {
        for (var t = 0; t < this.length; t++)
            e.apply(this, [this[t], t, this])
    }
    )
}
, function(e, t, n) {
    t = function(e, t, n) {
        var i = function() {}
          , o = new Object;
        o.superclass = Object,
        o.__NAME__ = "Object",
        o.superinstance = new Object,
        o.callsuper = function(e) {
            var t;
            this._realsuper ? this._realsuper = this._realsuper.prototype.superclass : this._realsuper = this.superclass,
            "string" == typeof e ? (t = Array.prototype.slice.call(arguments, 1),
            this._realsuper.prototype[e].apply(this, t)) : (t = Array.prototype.slice.call(arguments, 0),
            this._realsuper.apply(this, t)),
            this._realsuper = null
        }
        ,
        i.prototype = o,
        n.exports = i
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, o) {
    t = function(e, t, n) {
        var i = o(32);
        n.exports = function(e) {
            e = i(e);
            return "string" == typeof e ? e = decodeURIComponent(e) : null
        }
    }
    .call(t, o, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, o) {
    t = function(e, t, n) {
        var i = o(18);
        n.exports = function(e) {
            if (i(e)) {
                e = new RegExp("(^| )" + e + "=([^;]*)(;|$)").exec(document.cookie);
                if (e)
                    return e[2] || null
            }
            return null
        }
    }
    .call(t, o, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, o) {
    t = function(e, t, n) {
        var i = o(19);
        n.exports = function(e, t, n) {
            i(e, encodeURIComponent(t), n)
        }
    }
    .call(t, o, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, o) {
    t = function(e, t, n) {
        var i = o(19);
        n.exports = function(e, t) {
            (t = t || {}).expires = new Date(0),
            i(e, "", t)
        }
    }
    .call(t, o, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, o) {
    t = function(e, t, n) {
        var i = o(11);
        n.exports = i("Floater", {
            "construct": function(e) {
                e = e || {},
                this._view = e.view,
                this._valid = !0
            },
            "methods": {
                "show": function(e) {
                    e = e || {},
                    this._view.show(e)
                },
                "destroy": function() {
                    this._valid && (this._view.destroy && this._view.destroy(),
                    this._valid = !1)
                }
            }
        })
    }
    .call(t, o, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, a) {
    t = function(e, t, n) {
        var i = a(37)
          , o = a(38)
          , s = a(11);
        n.exports = s("FloaterView", {
            "construct": function(e) {
                e = e || {},
                this._panel = e.panel || document.body,
                this._zIndex = e.zIndex || 100,
                this.domHeight = e.domHeight,
                this.resetSize = e.resetSize
            },
            "methods": {
                "create": function() {
                    this._elem || (this._elem = document.createElement("div"),
                    this._elem.style.position = "absolute",
                    this._elem.style.top = "0px",
                    this._elem.style.zIndex = this._zIndex,
                    this._elem.style.visibility = "hidden",
                    this._panel.appendChild(this._elem),
                    this.adjustBind = this.adjustBind || this.adjustPosition.bind(this))
                },
                "show": function(e) {
                    this.create(),
                    this.build(e),
                    this.adjustPosition(),
                    this.doOnresize(),
                    this._elem.style.visibility = "visible",
                    this.showCover(),
                    this.winObj && (this.winObj.addEventListener ? this.winObj.addEventListener("resize", this.adjustBind) : this.winObj.attachEvent && this.winObj.attachEvent("onresize", this.adjustBind))
                },
                "destroy": function() {
                    this.hide(),
                    this.hideCover(),
                    this._removeEvent(),
                    this._removeDom()
                },
                "hide": function() {
                    this._elem.style.visibility = "visible"
                },
                "hideCover": function() {
                    o.hide()
                },
                "build": function(e) {
                    var t;
                    e.id ? (t = document.getElementById(e.id)) && (this._elem.appendChild(t),
                    e.removeBlock ? t.style = "" : t.style.display = "block") : e.html ? this._elem.innerHTML = e.html : e.elem && (e.replace && (this._elem.innerHTML = ""),
                    this._elem.appendChild(e.elem),
                    e.iframeId && e.url && (document.getElementById(e.iframeId).src = e.url),
                    e.elem.style.display = "block")
                },
                "adjustPosition": function() {
                    i(this._elem, {
                        "domHeight": this.domHeight,
                        "resetSize": this.resetSize
                    }),
                    o.resize(),
                    this._elem.offsetTop < 0 && (this._elem.style.top = "30px")
                },
                "showCover": function(e) {
                    o.show(this._zIndex - 5, e)
                },
                "_removeDom": function() {
                    var e = this._elem;
                    e.parentNode && setTimeout(function() {
                        e.parentNode.removeChild(e)
                    }, 0)
                },
                "_removeEvent": function() {
                    this.winObj && (this.winObj.addEventListener ? this.winObj.removeEventListener("resize", this.adjustBind) : this.winObj.attachEvent && this.winObj.detachEvent("onresize", this.adjustBind),
                    this.winObj = null)
                },
                "doOnresize": function() {
                    this.f || (this.winObj = window,
                    this.adjustBind = this.adjustBind || this.adjustPosition.bind(this),
                    this.winObj.addEventListener ? this.winObj.addEventListener("resize", this.adjustBind) : this.winObj.attachEvent && this.winObj.attachEvent("onresize", this.adjustBind))
                }
            }
        })
    }
    .call(t, a, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, i) {
    t = function(e, t, n) {
        var a = i(20)
          , r = i(21)
          , c = i(22)
          , d = i(23);
        n.exports = function(e, t) {
            var n, i, o, s;
            t = t || {},
            e && (s = e.offsetWidth || 360,
            n = t.domHeight || e.offsetHeight,
            o = r(),
            i = a(),
            o = (o - s) / 2 + c(),
            s = (i - n) / 2 + d(),
            e.style.position = "fixed",
            t.resetSize && (s = (i - n) / 2,
            e.style.left = o + "px",
            e.style.top = s + "px"))
        }
    }
    .call(t, i, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, a) {
    t = function(e, t, n) {
        var i = a(11)
          , o = a(14)
          , s = i("Overlay", {
            "_overlay": null,
            "statics": {
                "_count": 0,
                "_originZIndex": [],
                "show": function(e, t) {
                    var n;
                    t = t || {},
                    s._overlay || ((n = document.createElement("div")).style.position = o.IE6 ? "absolute" : "fixed",
                    n.style.left = "0",
                    n.style.top = "0",
                    n.style.width = "100%",
                    n.style.height = "100%",
                    n.style.background = t.bg || "#000",
                    n.style.opacity = t.opacity || "0.5",
                    n.style.filter = "alpha(opacity=" + (100 * t.opacity || 50) + ")",
                    n.style["-moz-opacity"] = t.opacity || "0.5",
                    n.setAttribute("data-loginIfr-layer", "loginIfrLayer"),
                    document.body.appendChild(n),
                    s._overlay = n),
                    e && (s._overlay.style.zIndex = e),
                    this.resize(),
                    s._overlay.style.display = ""
                },
                "hide": function() {
                    if (s._overlay) {
                        if (0 < s._count)
                            return s._count--,
                            void (s._overlay.style.zIndex = s._originZIndex[s._count]);
                        s._overlay.style.display = "none",
                        s._overlay.style.zIndex = 100
                    }
                },
                "resize": function() {}
            }
        });
        n.exports = s
    }
    .call(t, a, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        var a = {};
        n.exports = function(e) {
            if (e) {
                var t = new Image
                  , n = "slog_" + Math.floor(2147483648 * Math.random()).toString(36);
                (a[n] = t).onload = t.onerror = t.onabort = function() {
                    t.onload = t.onerror = t.onabort = null,
                    a[n] = null,
                    delete a[n],
                    t = null
                }
                ;
                var i, o = [];
                for (i in e)
                    o.push(i + "=" + encodeURIComponent(e[i]));
                try {
                    t.src = "//msg.qy.net/act?" + o.join("&")
                } catch (s) {}
            }
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        n.exports = function() {
            var e = window.document
              , t = e.body
              , n = e.documentElement
              , e = "BackCompat" == e.compatMode ? t : e.documentElement;
            return Math.max(n.scrollWidth, t.scrollWidth, e.clientWidth)
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        n.exports = function() {
            var e = window.document
              , t = e.body
              , n = e.documentElement
              , e = "BackCompat" == e.compatMode ? t : e.documentElement;
            return Math.max(n.scrollHeight, t.scrollHeight, e.clientHeight)
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        var c, u, p, h, g, f, m, i = (c = function(e, t) {
            return e << t | e >>> 32 - t
        }
        ,
        u = function(e, t) {
            var n = 2147483648 & e
              , i = 2147483648 & t
              , o = 1073741824 & e
              , s = 1073741824 & t
              , t = (1073741823 & e) + (1073741823 & t);
            return o & s ? 2147483648 ^ t ^ n ^ i : o | s ? 1073741824 & t ? 3221225472 ^ t ^ n ^ i : 1073741824 ^ t ^ n ^ i : t ^ n ^ i
        }
        ,
        p = function(e, t, n, i, o, s, a) {
            var r;
            return e = u(e, u(u((r = t) & n | ~r & i, o), a)),
            u(c(e, s), t)
        }
        ,
        h = function(e, t, n, i, o, s, a) {
            return e = u(e, u(u(t & (i = i) | n & ~i, o), a)),
            u(c(e, s), t)
        }
        ,
        g = function(e, t, n, i, o, s, a) {
            return e = u(e, u(u(t ^ n ^ i, o), a)),
            u(c(e, s), t)
        }
        ,
        f = function(e, t, n, i, o, s, a) {
            return e = u(e, u(u(n ^ (t | ~i), o), a)),
            u(c(e, s), t)
        }
        ,
        m = function(e) {
            for (var t = "", n = "", i = 0; i <= 3; i++)
                t += (n = "0" + (e >>> 8 * i & 255).toString(16)).substr(n.length - 2, 2);
            return t
        }
        ,
        function(e) {
            e += "";
            for (var t, n, i, o, s = Array(), s = function(e) {
                for (var t, n = e.length, i = n + 8, i = 16 * (1 + (i - i % 64) / 64), o = Array(i - 1), s = 0, a = 0; a < n; )
                    s = a % 4 * 8,
                    o[t = (a - a % 4) / 4] = o[t] | e.charCodeAt(a) << s,
                    a++;
                return s = a % 4 * 8,
                o[t = (a - a % 4) / 4] = o[t] | 128 << s,
                o[i - 2] = n << 3,
                o[i - 1] = n >>> 29,
                o
            }(e = function(e) {
                e = e.replace(/\x0d\x0a/g, "\n");
                for (var t = "", n = 0; n < e.length; n++) {
                    var i = e.charCodeAt(n);
                    i < 128 ? t += String.fromCharCode(i) : (127 < i && i < 2048 ? t += String.fromCharCode(i >> 6 | 192) : (t += String.fromCharCode(i >> 12 | 224),
                    t += String.fromCharCode(i >> 6 & 63 | 128)),
                    t += String.fromCharCode(63 & i | 128))
                }
                return t
            }(e)), a = 1732584193, r = 4023233417, c = 2562383102, d = 271733878, l = 0; l < s.length; l += 16)
                a = p(t = a, n = r, i = c, o = d, s[l + 0], 7, 3614090360),
                d = p(d, a, r, c, s[l + 1], 12, 3905402710),
                c = p(c, d, a, r, s[l + 2], 17, 606105819),
                r = p(r, c, d, a, s[l + 3], 22, 3250441966),
                a = p(a, r, c, d, s[l + 4], 7, 4118548399),
                d = p(d, a, r, c, s[l + 5], 12, 1200080426),
                c = p(c, d, a, r, s[l + 6], 17, 2821735955),
                r = p(r, c, d, a, s[l + 7], 22, 4249261313),
                a = p(a, r, c, d, s[l + 8], 7, 1770035416),
                d = p(d, a, r, c, s[l + 9], 12, 2336552879),
                c = p(c, d, a, r, s[l + 10], 17, 4294925233),
                r = p(r, c, d, a, s[l + 11], 22, 2304563134),
                a = p(a, r, c, d, s[l + 12], 7, 1804603682),
                d = p(d, a, r, c, s[l + 13], 12, 4254626195),
                c = p(c, d, a, r, s[l + 14], 17, 2792965006),
                r = p(r, c, d, a, s[l + 15], 22, 1236535329),
                a = h(a, r, c, d, s[l + 1], 5, 4129170786),
                d = h(d, a, r, c, s[l + 6], 9, 3225465664),
                c = h(c, d, a, r, s[l + 11], 14, 643717713),
                r = h(r, c, d, a, s[l + 0], 20, 3921069994),
                a = h(a, r, c, d, s[l + 5], 5, 3593408605),
                d = h(d, a, r, c, s[l + 10], 9, 38016083),
                c = h(c, d, a, r, s[l + 15], 14, 3634488961),
                r = h(r, c, d, a, s[l + 4], 20, 3889429448),
                a = h(a, r, c, d, s[l + 9], 5, 568446438),
                d = h(d, a, r, c, s[l + 14], 9, 3275163606),
                c = h(c, d, a, r, s[l + 3], 14, 4107603335),
                r = h(r, c, d, a, s[l + 8], 20, 1163531501),
                a = h(a, r, c, d, s[l + 13], 5, 2850285829),
                d = h(d, a, r, c, s[l + 2], 9, 4243563512),
                c = h(c, d, a, r, s[l + 7], 14, 1735328473),
                r = h(r, c, d, a, s[l + 12], 20, 2368359562),
                a = g(a, r, c, d, s[l + 5], 4, 4294588738),
                d = g(d, a, r, c, s[l + 8], 11, 2272392833),
                c = g(c, d, a, r, s[l + 11], 16, 1839030562),
                r = g(r, c, d, a, s[l + 14], 23, 4259657740),
                a = g(a, r, c, d, s[l + 1], 4, 2763975236),
                d = g(d, a, r, c, s[l + 4], 11, 1272893353),
                c = g(c, d, a, r, s[l + 7], 16, 4139469664),
                r = g(r, c, d, a, s[l + 10], 23, 3200236656),
                a = g(a, r, c, d, s[l + 13], 4, 681279174),
                d = g(d, a, r, c, s[l + 0], 11, 3936430074),
                c = g(c, d, a, r, s[l + 3], 16, 3572445317),
                r = g(r, c, d, a, s[l + 6], 23, 76029189),
                a = g(a, r, c, d, s[l + 9], 4, 3654602809),
                d = g(d, a, r, c, s[l + 12], 11, 3873151461),
                c = g(c, d, a, r, s[l + 15], 16, 530742520),
                r = g(r, c, d, a, s[l + 2], 23, 3299628645),
                a = f(a, r, c, d, s[l + 0], 6, 4096336452),
                d = f(d, a, r, c, s[l + 7], 10, 1126891415),
                c = f(c, d, a, r, s[l + 14], 15, 2878612391),
                r = f(r, c, d, a, s[l + 5], 21, 4237533241),
                a = f(a, r, c, d, s[l + 12], 6, 1700485571),
                d = f(d, a, r, c, s[l + 3], 10, 2399980690),
                c = f(c, d, a, r, s[l + 10], 15, 4293915773),
                r = f(r, c, d, a, s[l + 1], 21, 2240044497),
                a = f(a, r, c, d, s[l + 8], 6, 1873313359),
                d = f(d, a, r, c, s[l + 15], 10, 4264355552),
                c = f(c, d, a, r, s[l + 6], 15, 2734768916),
                r = f(r, c, d, a, s[l + 13], 21, 1309151649),
                a = f(a, r, c, d, s[l + 4], 6, 4149444226),
                d = f(d, a, r, c, s[l + 11], 10, 3174756917),
                c = f(c, d, a, r, s[l + 2], 15, 718787259),
                r = f(r, c, d, a, s[l + 9], 21, 3951481745),
                a = u(a, t),
                r = u(r, n),
                c = u(c, i),
                d = u(d, o);
            return (m(a) + m(r) + m(c) + m(d)).toLowerCase()
        }
        );
        n.exports = i
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        n.exports = function(e, t) {
            for (var n in t)
                t.hasOwnProperty(n) && (e[n] = t[n]);
            return e
        }
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, i) {
    t = function(e, t, n) {
        var s = i(14);
        n.exports = function(e, t, n) {
            var i = null
              , o = null;
            if (t) {
                switch (o = document.getElementsByTagName("head")[0],
                e) {
                case "css":
                    (i = document.createElement("link")).rel = "stylesheet",
                    i.href = t;
                    break;
                case "js":
                    (i = document.createElement("script")).type = "text/javascript",
                    i.src = t
                }
                null != i && "object" == typeof i && o.appendChild(i),
                s.IE && i.readyState ? i.onreadystatechange = function() {
                    /loaded|complete/.test(i.readyState) && n && n()
                }
                : i.onload = function() {
                    n && n()
                }
            }
        }
    }
    .call(t, i, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t, n) {
    t = function(e, t, n) {
        var o, s, b, a = {}, w = {}, k = 65536, C = k - 1, P = function(e) {
            this.digits = "boolean" == typeof e && !0 === e ? null : o.slice(0),
            this.isNeg = !1
        };
        function r(e) {
            var t = w
              , n = t.biDivideByRadixPower(e, this.k - 1)
              , n = t.biMultiply(n, this.mu)
              , n = t.biDivideByRadixPower(n, this.k + 1)
              , e = t.biModuloByRadixPower(e, this.k + 1)
              , n = t.biMultiply(n, this.modulus)
              , n = t.biModuloByRadixPower(n, this.k + 1)
              , i = t.biSubtract(e, n);
            i.isNeg && (i = t.biAdd(i, this.bkplus1));
            for (var o = 0 <= t.biCompare(i, this.modulus); o; )
                i = t.biSubtract(i, this.modulus),
                o = 0 <= t.biCompare(i, this.modulus);
            return i
        }
        function c(e, t) {
            t = w.biMultiply(e, t);
            return this.modulo(t)
        }
        function d(e, t) {
            var n = new P;
            n.digits[0] = 1;
            for (var i = e, o = t; 0 != (1 & o.digits[0]) && (n = this.multiplyMod(n, i)),
            0 != (o = w.biShiftRight(o, 1)).digits[0] || 0 != w.biHighIndex(o); )
                i = this.multiplyMod(i, i);
            return n
        }
        a.BarrettMu = function(e) {
            this.modulus = w.biCopy(e),
            this.k = w.biHighIndex(this.modulus) + 1;
            e = new P;
            e.digits[2 * this.k] = 1,
            this.mu = w.biDivide(e, this.modulus),
            this.bkplus1 = new P,
            this.bkplus1.digits[this.k + 1] = 1,
            this.modulo = r,
            this.multiplyMod = c,
            this.powMod = d
        }
        ,
        w.biModuloByRadixPower = function(e, t) {
            var n = new P;
            return w.arrayCopy(e.digits, 0, n.digits, 0, t),
            n
        }
        ,
        w.biMultiply = function(e, t) {
            for (var n, i, o, s = new P, a = w.biHighIndex(e), r = w.biHighIndex(t), c = 0; c <= r; ++c) {
                for (o = c,
                j = n = 0; j <= a; ++j,
                ++o)
                    i = s.digits[o] + e.digits[j] * t.digits[c] + n,
                    s.digits[o] = i & C,
                    n = i >>> 16;
                s.digits[c + a + 1] = n
            }
            return s.isNeg = e.isNeg != t.isNeg,
            s
        }
        ,
        w.biDivideByRadixPower = function(e, t) {
            var n = new P;
            return w.arrayCopy(e.digits, t, n.digits, 0, n.digits.length - t),
            n
        }
        ,
        w.biDivide = function(e, t) {
            return w.biDivideModulo(e, t)[0]
        }
        ,
        w.setMaxDigits = function(e) {
            o = new Array(e);
            for (var t = 0; t < o.length; t++)
                o[t] = 0;
            s = new P,
            (b = new P).digits[0] = 1
        }
        ,
        w.setMaxDigits(20),
        w.biCopy = function(e) {
            var t = new P(!0);
            return t.digits = e.digits.slice(0),
            t.isNeg = e.isNeg,
            t
        }
        ,
        w.reverseStr = function(e) {
            for (var t = "", n = e.length - 1; -1 < n; --n)
                t += e.charAt(n);
            return t
        }
        ;
        var l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
        w.biToString = function(e, t) {
            var n = new P;
            n.digits[0] = t;
            for (var i = w.biDivideModulo(e, n), o = l[i[1].digits[0]]; 1 == w.biCompare(i[0], s); )
                i = w.biDivideModulo(i[0], n),
                digit = i[1].digits[0],
                o += l[i[1].digits[0]];
            return (e.isNeg ? "-" : "") + w.reverseStr(o)
        }
        ;
        var u = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
        w.digitToHex = function(e) {
            var t = "";
            for (i = 0; i < 4; ++i)
                t += u[15 & e],
                e >>>= 4;
            return w.reverseStr(t)
        }
        ,
        w.biToHex = function(e) {
            for (var t = "", n = (w.biHighIndex(e),
            w.biHighIndex(e)); -1 < n; --n)
                t += w.digitToHex(e.digits[n]);
            return t
        }
        ,
        w.charToHex = function(e) {
            e = 48 <= e && e <= 57 ? e - 48 : 65 <= e && e <= 90 ? 10 + e - 65 : 97 <= e && e <= 122 ? 10 + e - 97 : 0;
            return e
        }
        ,
        w.hexToDigit = function(e) {
            for (var t = 0, n = Math.min(e.length, 4), i = 0; i < n; ++i)
                t <<= 4,
                t |= w.charToHex(e.charCodeAt(i));
            return t
        }
        ,
        w.biFromHex = function(e) {
            for (var t = new P, n = e.length, i = 0; 0 < n; n -= 4,
            ++i)
                t.digits[i] = w.hexToDigit(e.substr(Math.max(n - 4, 0), Math.min(n, 4)));
            return t
        }
        ,
        w.biAdd = function(e, t) {
            var n;
            if (e.isNeg != t.isNeg)
                t.isNeg = !t.isNeg,
                n = w.biSubtract(e, t),
                t.isNeg = !t.isNeg;
            else {
                n = new P;
                for (var i, o = 0, s = 0; s < e.digits.length; ++s)
                    i = e.digits[s] + t.digits[s] + o,
                    n.digits[s] = i % k,
                    o = Number(k <= i);
                n.isNeg = e.isNeg
            }
            return n
        }
        ,
        w.biSubtract = function(e, t) {
            if (e.isNeg != t.isNeg)
                t.isNeg = !t.isNeg,
                i = w.biAdd(e, t),
                t.isNeg = !t.isNeg;
            else {
                for (var n, i = new P, o = 0, s = 0; s < e.digits.length; ++s)
                    n = e.digits[s] - t.digits[s] + o,
                    i.digits[s] = n % k,
                    i.digits[s] < 0 && (i.digits[s] += k),
                    o = 0 - Number(n < 0);
                if (-1 == o) {
                    for (s = o = 0; s < e.digits.length; ++s)
                        n = 0 - i.digits[s] + o,
                        i.digits[s] = n % k,
                        i.digits[s] < 0 && (i.digits[s] += k),
                        o = 0 - Number(n < 0);
                    i.isNeg = !e.isNeg
                } else
                    i.isNeg = e.isNeg
            }
            return i
        }
        ,
        w.biHighIndex = function(e) {
            for (var t = e.digits.length - 1; 0 < t && 0 == e.digits[t]; )
                --t;
            return t
        }
        ,
        w.biNumBits = function(e) {
            for (var t = w.biHighIndex(e), n = e.digits[t], i = 16 * (t + 1), o = i; i - 16 < o && 0 == (32768 & n); --o)
                n <<= 1;
            return o
        }
        ,
        w.biMultiplyDigit = function(e, t) {
            var n, i, o;
            result = new P,
            n = w.biHighIndex(e);
            for (var s = i = 0; s <= n; ++s)
                o = result.digits[s] + e.digits[s] * t + i,
                result.digits[s] = o & C,
                i = o >>> 16;
            return result.digits[1 + n] = i,
            result
        }
        ,
        w.arrayCopy = function(e, t, n, i, o) {
            for (var s = Math.min(t + o, e.length), a = t, r = i; a < s; ++a,
            ++r)
                n[r] = e[a]
        }
        ;
        var p = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535];
        w.biShiftLeft = function(e, t) {
            var n = Math.floor(t / 16)
              , i = new P;
            w.arrayCopy(e.digits, 0, i.digits, n, i.digits.length - n);
            for (var o = t % 16, s = 16 - o, a = i.digits.length - 1, r = a - 1; 0 < a; --a,
            --r)
                i.digits[a] = i.digits[a] << o & C | (i.digits[r] & p[o]) >>> s;
            return i.digits[0] = i.digits[a] << o & C,
            i.isNeg = e.isNeg,
            i
        }
        ;
        var h = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535];
        w.biShiftRight = function(e, t) {
            var n = Math.floor(t / 16)
              , i = new P;
            w.arrayCopy(e.digits, n, i.digits, 0, e.digits.length - n);
            for (var o = t % 16, s = 16 - o, a = 0, r = a + 1; a < i.digits.length - 1; ++a,
            ++r)
                i.digits[a] = i.digits[a] >>> o | (i.digits[r] & h[o]) << s;
            return i.digits[i.digits.length - 1] >>>= o,
            i.isNeg = e.isNeg,
            i
        }
        ,
        w.biMultiplyByRadixPower = function(e, t) {
            var n = new P;
            return w.arrayCopy(e.digits, 0, n.digits, t, n.digits.length - t),
            n
        }
        ,
        w.biCompare = function(e, t) {
            if (e.isNeg != t.isNeg)
                return 1 - 2 * Number(e.isNeg);
            for (var n = e.digits.length - 1; 0 <= n; --n)
                if (e.digits[n] != t.digits[n])
                    return e.isNeg ? 1 - 2 * Number(e.digits[n] > t.digits[n]) : 1 - 2 * Number(e.digits[n] < t.digits[n]);
            return 0
        }
        ,
        w.biDivideModulo = function(e, t) {
            var n, i, o = w.biNumBits(e), s = w.biNumBits(t), a = t.isNeg;
            if (o < s)
                return e.isNeg ? ((n = w.biCopy(b)).isNeg = !t.isNeg,
                e.isNeg = !1,
                t.isNeg = !1,
                i = biSubtract(t, e),
                e.isNeg = !0,
                t.isNeg = a) : (n = new P,
                i = w.biCopy(e)),
                [n, i];
            n = new P,
            i = e;
            for (var r = Math.ceil(s / 16) - 1, c = 0; t.digits[r] < 32768; )
                t = w.biShiftLeft(t, 1),
                ++c,
                ++s,
                r = Math.ceil(s / 16) - 1;
            i = w.biShiftLeft(i, c),
            o += c;
            for (var d = Math.ceil(o / 16) - 1, l = w.biMultiplyByRadixPower(t, d - r); -1 != w.biCompare(i, l); )
                ++n.digits[d - r],
                i = w.biSubtract(i, l);
            for (var u = d; r < u; --u) {
                var p = u >= i.digits.length ? 0 : i.digits[u]
                  , h = u - 1 >= i.digits.length ? 0 : i.digits[u - 1]
                  , g = u - 2 >= i.digits.length ? 0 : i.digits[u - 2]
                  , f = r >= t.digits.length ? 0 : t.digits[r]
                  , m = r - 1 >= t.digits.length ? 0 : t.digits[r - 1];
                n.digits[u - r - 1] = p == f ? C : Math.floor((p * k + h) / f);
                for (var v = n.digits[u - r - 1] * (f * k + m), y = 4294967296 * p + (h * k + g); y < v; )
                    --n.digits[u - r - 1],
                    v = n.digits[u - r - 1] * (f * k | m),
                    y = p * k * k + (h * k + g);
                l = w.biMultiplyByRadixPower(t, u - r - 1),
                (i = w.biSubtract(i, w.biMultiplyDigit(l, n.digits[u - r - 1]))).isNeg && (i = w.biAdd(i, l),
                --n.digits[u - r - 1])
            }
            return i = w.biShiftRight(i, c),
            n.isNeg = e.isNeg != a,
            e.isNeg && (n = a ? w.biAdd(n, b) : w.biSubtract(n, b),
            t = w.biShiftRight(t, c),
            i = w.biSubtract(t, i)),
            0 == i.digits[0] && 0 == w.biHighIndex(i) && (i.isNeg = !1),
            [n, i]
        }
        ;
        var g = function(e, t, n) {
            var i = w;
            this.e = i.biFromHex(e),
            this.d = i.biFromHex(t),
            this.m = i.biFromHex(n),
            this.chunkSize = 2 * i.biHighIndex(this.m),
            this.radix = 16,
            this.barrett = new a.BarrettMu(this.m)
        };
        w.getKeyPair = function(e, t, n) {
            return new g(e,t,n)
        }
        ,
        w.encryptedString = function(e, t) {
            for (var n = [], i = t.length, o = 0; o < i; )
                n[o] = t.charCodeAt(o),
                o++;
            for (; n.length % e.chunkSize != 0; )
                n[o++] = 0;
            for (var s, a, r, c = n.length, d = "", o = 0; o < c; o += e.chunkSize) {
                for (r = new P,
                s = 0,
                a = o; a < o + e.chunkSize; ++s)
                    r.digits[s] = n[a++],
                    r.digits[s] += n[a++] << 8;
                var l = e.barrett.powMod(r, e.e);
                d += (16 == e.radix ? w.biToHex(l) : w.biToString(l, e.radix)) + " "
            }
            return d.substring(0, d.length - 1)
        }
        ,
        w.setMaxDigits(130),
        n.exports = w
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(t, n, P) {
    (function(C) {
        var e = function(e, t, n) {
            var i = P(47)
              , o = P(6)
              , s = P(48)
              , a = P(58)
              , r = P(61)
              , c = P(65)
              , d = P(74)
              , l = P(4)
              , u = P(3)
              , p = P(75)
              , h = P(1)
              , g = P(2)
              , f = P(76)
              , m = P(8)
              , v = P(15).getDomain()
              , y = P(9)
              , b = ""
              , w = "icon-login__pwd"
              , k = "icon-login__qrcode";
            n.exports = C.Class("indexAction", {
                "extend": o,
                "construct": function() {},
                "methods": {
                    "openLoginRegWindow": function(e) {
                        e.types = e.types || (5 == e.firstShow ? "" : "1,2,3,4,5"),
                        g.initConfig(e),
                        b = g.getConfig();
                        var t = this;
                        this.config = C.extend({
                            "agenttype": b.agenttype,
                            "ptid": b.ptid,
                            "skinMode": b.skinMode,
                            "protocolDom": b.protocolDom,
                            "logoUrl": b.logoUrl
                        }, e),
                        this.createFloater();
                        var n = document.querySelector('[data-login-sdk="panel"]');
                        this.doms = {
                            "baseLoginPanel": n.querySelector('[data-login-sdk="baseLogin"]'),
                            "scanLoginPanel": n.querySelector('[data-login-sdk="scanLogin"]'),
                            "smsLoginRegPanel": n.querySelector('[data-login-sdk="smsLoginreg"]'),
                            "thridPartyPanel": n.querySelector('[data-login-sdk="thridPartyLogin"]'),
                            "regPanel": n.querySelector('[data-login-sdk="reg"]'),
                            "realNamePanel": n.querySelector('[data-login-sdk="realname"]'),
                            "upSmsCodePanel": n.querySelector('[data-login-sdk="upSmsCode"]'),
                            "closeBtn": n.querySelector('[data-login-sdk="close"]'),
                            "toastPanel": n.querySelector('[data-login-sdk="toast"]'),
                            "leftIconPanel": n.querySelector('[data-login-sdk="leftIcon"]'),
                            "leftIcon": n.querySelector('[data-login-sdk="leftIcon"]').children[0],
                            "protocolPanel": n.querySelector('[data-login-sdk="protocol"]'),
                            "slideCover": n.querySelector('[data-login-sdk="slideCover"]'),
                            "slidePanel": n.querySelector('[data-login-sdk="slidePanel"]'),
                            "verifyPhonePanel": n.querySelector('[data-login-sdk="verifyPhone"]'),
                            "logoImg": n.querySelector('[data-login-sdk="logoImg"]'),
                            "regProtocolPanel": n.querySelector('[data-login-sdk="regProtocol"]')
                        },
                        this.config.hideClose && u.addClass(this.doms.closeBtn, "dn"),
                        "pca" == this.config.business && u.addClass(n, "qy-login-pca"),
                        this.verifyCenter = new d({
                            "slideCover": this.doms.slideCover,
                            "slidePanel": this.doms.slidePanel
                        }),
                        this.verifyCenter.init(function() {
                            window.VerifyCenter && window.VerifyCenter.collect && window.VerifyCenter.collect.init({
                                "ignoreJsBridge": !0
                            })
                        }),
                        this.showPanel = null,
                        this.prePanel = null,
                        this.showType = -1,
                        this.localCookie = {};
                        var i = C.cookie.get("QC160")
                          , e = 1;
                        i && ("p1" == (e = JSON.parse(i).type || 1) ? e = 1 : "s1" == e && (e = 2),
                        this.localCookie = JSON.parse(i)),
                        this.initLoginTypes(),
                        this.defaultShowType = e,
                        this.config.logoUrl && (this.doms.logoImg.src = this.config.logoUrl),
                        this.config.logoHeight && (this.doms.logoImg.style.height = this.config.logoHeight + "px"),
                        this.bindEvent(),
                        setTimeout(function() {
                            t.toggelLoginPanel(),
                            u.removeClass(n, "dn")
                        }, 10)
                    },
                    "initLoginTypes": function() {
                        var e = this.config.types;
                        (e.indexOf(1) < 0 && e.indexOf(3) < 0 || e.indexOf(2) < 0) && u.addClass(this.doms.leftIcon, "dn"),
                        this.config.protocolDom && (this.doms.protocolPanel.innerHTML = this.config.protocolDom)
                    },
                    "toggelLoginPanel": function(e, t, n) {
                        e = e || this.config.firstShow || this.defaultShowType;
                        switch (e = parseInt(e)) {
                        case 1:
                            this.initBaseLogin();
                            break;
                        case 2:
                            this.initScanLogin();
                            break;
                        case 3:
                            this.initSmsLogin();
                            break;
                        case 4:
                            this.initRegist();
                            break;
                        case 5:
                            this.initRealName(t, n);
                            break;
                        default:
                            this.initBaseLogin()
                        }
                        4 != e && 0 <= this.config.types.indexOf(4) && this.initThirdLogin(e)
                    },
                    "initBaseLogin": function() {
                        this.baseLogin || (this.baseLogin = new s({
                            "panel": this.doms.baseLoginPanel,
                            "types": this.config.types,
                            "verifyCenter": this.verifyCenter,
                            "toastPanel": this.doms.toastPanel,
                            "business": this.config.business,
                            "errMsg": this.config.errMsg
                        }),
                        this.baseLogin.init()),
                        this.baseLogin.showPanel(),
                        this.resetAcode(this.baseLogin),
                        this.showPanel = this.doms.baseLoginPanel,
                        this.showType = 1
                    },
                    "initSmsLogin": function() {
                        this.smsLoginReg || (this.smsLoginReg = new c({
                            "panel": this.doms.smsLoginRegPanel,
                            "types": this.config.types,
                            "upSmsCodePanel": this.doms.upSmsCodePanel,
                            "verifyCenter": this.verifyCenter
                        }),
                        this.smsLoginReg.init()),
                        this.smsLoginReg.showPanel(),
                        this.resetAcode(this.smsLoginReg),
                        this.showPanel = this.doms.smsLoginRegPanel,
                        this.showType = 3
                    },
                    "initThirdLogin": function(e) {
                        this.thridParty || (this.thridParty = new r({
                            "panel": this.doms.thridPartyPanel,
                            "verifyCenter": this.verifyCenter,
                            "types": this.config.thirds,
                            "toastPanel": this.doms.toastPanel,
                            "business": this.config.business,
                            "thirdLoginCB": this.config.thirdLoginCB
                        }),
                        this.thridParty.init(),
                        u.removeClass(this.doms.thridPartyPanel, "dn")),
                        this.sendThridPartyBlock(e)
                    },
                    "initScanLogin": function(e) {
                        var t = "normal"
                          , n = "";
                        e && (t = e.type || "normal",
                        n = e.msg || e.mobile || ""),
                        this.scanLogin || (this.scanLogin = new a({
                            "type": t,
                            "msg": n,
                            "business": this.config.business,
                            "appTitle": this.config.appTitle,
                            "panel": this.doms.scanLoginPanel
                        }),
                        this.scanLogin.init()),
                        u.addClass(this.showPanel, "dn"),
                        this.scanLogin.showPanel({
                            "type": t,
                            "msg": n
                        }),
                        2 != this.showType && (-1 == this.showType ? !this.config.types || 0 <= this.config.types.indexOf("1") ? this.preShowType = 1 : this.preShowType = 3 : this.preShowType = this.showType),
                        this.showPanel = this.doms.scanLoginPanel,
                        "normal" == t ? (this.showType = 2,
                        this.toggleIcon(w, k),
                        this.toggleSpecialPanel(!0)) : u.hasClass(this.doms.leftIconPanel, "dn") || this.toggleSpecialPanel()
                    },
                    "toggleSpecialPanel": function(e, t, n) {
                        e ? ("3" != e && (u.removeClass(this.doms.thridPartyPanel, "dn"),
                        n && this.sendThridPartyBlock(this.showType),
                        u.removeClass(this.doms.leftIconPanel, "dn")),
                        u.removeClass(this.doms.protocolPanel, "dn")) : (u.addClass(this.doms.thridPartyPanel, "dn"),
                        u.addClass(this.doms.leftIconPanel, "dn"),
                        t || u.addClass(this.doms.protocolPanel, "dn"))
                    },
                    "initRegist": function() {
                        var e = this.doms.regPanel;
                        this.regIns || (this.regIns = new c({
                            "panel": e,
                            "upSmsCodePanel": this.doms.upSmsCodePanel,
                            "verifyCenter": this.verifyCenter,
                            "type": "reg"
                        }),
                        this.regIns.init()),
                        this.toggleSpecialPanel("", !0),
                        this.regIns.showPanel(),
                        this.resetAcode(this.regIns),
                        this.showPanel = e
                    },
                    "initRealName": function(e, t) {
                        var n = this.doms.realNamePanel;
                        this.realNameIns = new c({
                            "panel": n,
                            "upSmsCodePanel": this.doms.upSmsCodePanel,
                            "verifyCenter": this.verifyCenter,
                            "type": "realname",
                            "hideBack": 5 == this.config.firstShow,
                            "token": e,
                            "verifyPhonePanel": this.doms.verifyPhonePanel,
                            "loginSucRpage": t
                        }),
                        this.realNameIns.init(),
                        this.resetAcode(this.realNameIns),
                        this.toggleSpecialPanel("", !0),
                        this.realNameIns.showPanel()
                    },
                    "bindEvent": function() {
                        var n = this;
                        h.on(this.doms.closeBtn, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            n.closeFloater()
                        });
                        h.on(this.doms.leftIconPanel, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            u.addClass(n.showPanel, "dn"),
                            u.hasClass(n.doms.leftIcon, k) ? (n.toggleIcon(w, k),
                            n.initScanLogin(),
                            n.sendThridPartyBlock(2),
                            m.click({
                                "rpage": "passsdk",
                                "block": 1 == n.preShowType ? "psprt_acc" : "psprt_sms",
                                "rseat": 1 == n.preShowType ? "acc2QR" : "sms2QR"
                            })) : (m.click({
                                "rpage": "passsdk",
                                "block": "psprt_QRcode",
                                "rseat": "QR2acc"
                            }),
                            n.toggleIcon(k, w),
                            n.scanLogin && n.scanLogin.hidePanel(),
                            n.toggelLoginPanel(n.preShowType))
                        });
                        var t = this.doms.protocolPanel.querySelector('[data-protocol-btn="agree"]');
                        t && ("2" == this.config.types && "2" == this.config.firstShow ? u.addClass(t, "dn") : h.on(t, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            u.hasClass(t, "selected") ? u.removeClass(t, "selected") : u.addClass(t, "selected")
                        })),
                        l.on("showQrCodeLogin", function(e) {
                            n.initScanLogin(e.data)
                        }),
                        l.on("handleLoginSuc", function(e) {
                            n.showLoginToast(e);
                            var t = null;
                            "pca" == n.config.business && "login_scs_acc" === e.data.rpage && (t = n.baseLogin.getAutoLoginStatus(),
                            e.auto_login = t),
                            n.updateInfo && 0 <= e.data.rpage.indexOf("login_scs_3") && (e.data.isNewUser = !0),
                            n.notify({
                                "type": "login",
                                "data": e
                            }),
                            e.data && e.data.rpage && e.data.rpage.indexOf("login_scs_3") < 0 && (e = {
                                "type": n.showType
                            },
                            null != t ? e.autoLogin = t : "pca" == n.config.business && n.localCookie.autoLogin != undefined && (e.autoLogin = n.localCookie.autoLogin),
                            C.cookie.set("QC160", JSON.stringify(e), {
                                "expires": 31536e6,
                                "path": "/",
                                "domain": v
                            })),
                            setTimeout(function() {
                                n.closeFloater()
                            }, 2e3),
                            "pca" != n.config.business && f.request()
                        }),
                        l.on("backShow", function(e) {
                            e.data.resetShowPanel && 2 == n.showType ? (n.initScanLogin(),
                            n.sendThridPartyBlock(2)) : (n.toggelLoginPanel(n.showType),
                            n.toggleSpecialPanel(!0)),
                            e.data.resetSize && n.resetSize(440)
                        }),
                        l.on("toggleSpecialPanel", function(e) {
                            n.toggleSpecialPanel(e.data, "", !0)
                        }),
                        l.on("toggleLoginTypes", function(e) {
                            u.addClass(n.showPanel, "dn"),
                            4 != e.data.type && (n.toggleSpecialPanel(!0),
                            2 == n.showType && u.hasClass(n.doms.leftIcon, w) && n.toggleIcon(k, w)),
                            n.toggelLoginPanel(e.data.type, e.data.token, e.data.rpage),
                            4 != e.data.type && 5 != e.data.type || n.resetSize(390)
                        }),
                        l.on("globalAcodeChange", function(e) {
                            n.acode = e.data.acode,
                            n.aname = e.data.name
                        }),
                        l.on("setUpdateInfo", function(e) {
                            n.updateInfo = e.data.updateInfo
                        }),
                        l.on("resizeHeight", function(e) {
                            n.resetSize(e.data)
                        })
                    },
                    "resetAcode": function(e) {
                        this.acode && e.resetAcode(this.acode, this.aname)
                    },
                    "showLoginToast": function(e) {
                        var t = {
                            "title": "登录成功"
                        };
                        e.data && e.data.icon && (t = {
                            "title": e.data.isNewUser ? "恭喜，注册成功～" : "登录成功",
                            "tip": e.data.isNewUser ? "下面是您将在爱奇艺使用的头像和昵称" : e.data.isReg ? "发现您曾经注册过爱奇艺账号，登录中……" : "",
                            "nickname": e.data.nickname || "一名用户",
                            "icon": e.data.icon
                        }),
                        this.config.hideIcon && (t.icon = ""),
                        this.config.hideNickname && (t.nickname = ""),
                        y.loginSuc(this.doms.toastPanel, t),
                        m.show({
                            "rpage": e.data.rpage
                        })
                    },
                    "toggleIcon": function(e, t) {
                        var n = this.doms.leftIcon;
                        u.addClass(n, e),
                        u.removeClass(n, t)
                    },
                    "sendThridPartyBlock": function(e) {
                        var t = 1 == e || 2 == e || 3 == e;
                        this.thridParty && t && (t = 1 == e ? this.doms.baseLoginPanel : 2 == e ? this.doms.scanLoginPanel : this.doms.smsLoginRegPanel,
                        this.thridParty.sendBlock(e, t))
                    },
                    "createFloater": function() {
                        var e = 440;
                        4 == this.config.firstShow || 5 == this.config.firstShow ? e = 390 : this.config.types.indexOf("4") < 0 && (e = 360),
                        this.floater || (this.floater = new C.floater({
                            "view": new C.floaterView({
                                "isResize": !1,
                                "zIndex": 9999,
                                "domHeight": e,
                                "resetSize": "pca" != this.config.business
                            })
                        })),
                        this.floater.show({
                            "html": i
                        }),
                        this.notify("pcLoginSDKShow")
                    },
                    "closeFloater": function() {
                        this.floater.destroy(),
                        this.doms = {},
                        h.unAll(),
                        l.unAll(b.globalEvent),
                        this.thridParty && this.thridParty.destroy(),
                        this.scanLogin && this.scanLogin.destroy(),
                        this.floater = null,
                        this.thridParty = null,
                        this.scanLogin = null,
                        this.baseLogin = null,
                        this.smsLoginReg = null,
                        this.regIns = null,
                        this.realNameIns = null,
                        this.showPanel = null,
                        this.prePanel = null,
                        this.showType = -1,
                        this.isSmsThirdLogin = !1,
                        this.acode = "",
                        this.aname = "",
                        this.updateInfo = !1,
                        this.notify("pcLoginSDKHide")
                    },
                    "logout": function(e) {
                        var t = this;
                        e = e || {},
                        p.request(e, function() {
                            t.notify("logout")
                        })
                    },
                    "notify": function(e) {
                        e = "string" == typeof e ? {
                            "type": e
                        } : e;
                        l.fire(e),
                        window.postMessage(e, window.location.href)
                    },
                    "resetSize": function(e) {
                        "pca" == this.config.business && (e = '{"call_type":"request", "cmd":"page_size_change", "cmd_context":"", "cmd_data":{"width":360,"height":' + e + "}}",
                        window.external.js_app_service(e))
                    }
                }
            })
        }
        .call(n, P, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, P(0))
}
, function(e, t) {
    e.exports = '<div class="qy-login-wrapper dn" data-login-sdk="panel"> <div class="qy-login-container"> <div class="qy-login-header"> <div class="header-qrCode" data-login-sdk="leftIcon"> <i class="icon-login icon-login__qrcode"></i> </div> <div class="header-logo"> <div class="header-logo-inner"> <img src="//www.iqiyipic.com/common/fix/login-logo-iqiyi.png" alt="" data-login-sdk="logoImg"> </div> </div> <span class="iconfont icon-close" data-login-sdk="close"></span> </div> <div class="qy-login-form"> <div class="login-form-inner"> <div class="login-form"> <div class="dn" data-login-sdk="baseLogin"></div> <div class="dn" data-login-sdk="scanLogin"></div> <div class="dn" data-login-sdk="smsLoginreg"></div> <div class="dn" data-login-sdk="baseLogin"></div> <div class="dn" data-login-sdk="reg"></div> <div class="dn" data-login-sdk="realname"></div> <div class="dn" data-login-sdk="verifyPhone"></div> <div class="dn" data-login-sdk="upSmsCode"></div> <div class="qy-login-sns dn" data-login-sdk="regProtocol"></div> <div class="qy-login-agreement" data-login-sdk="protocol"> <div class="agreement-link"><a href="javascript:;" data-protocol-btn="agree"><span class="iconfont icon-select"></span></a>同意<a href="https://www.iqiyi.com/user/register/protocol.html" class="theme-color" target="_blank">《用户协议》</a>和<a href="https://privacy.iqiyi.com/policies" class="theme-color" target="_blank">《隐私政策》</a></div> <div class="agreement-tips">新版《用户协议》已更新，请您及时查看</div> </div> <div class="qy-login-sns dn" data-login-sdk="thridPartyLogin"></div> </div> <div class="qy-login-cover dn" data-login-sdk="slideCover"> <div class="qy-login-slideVerify"> <div class="slideVerify-title">为保证您的账号安全，请完成以下认证</div> <div class="slideVerify-box" data-login-sdk="slidePanel"> </div> </div> </div> <div class="qy-login-cover dn" data-login-sdk="toast"></div> </div> </div> </div> </div>'
}
, function(t, n, b) {
    (function(y) {
        var e = function(e, t, n) {
            var i = b(6)
              , o = b(24)
              , s = b(54)
              , a = new (b(55))
              , r = b(1)
              , c = b(4)
              , d = b(3)
              , l = b(26)
              , u = b(8)
              , p = b(17)
              , h = b(9)
              , g = b(56)
              , f = "baseLoginAcodeChange"
              , m = "resetBaseLoginBtnStatus"
              , v = "login_scs_acc";
            n.exports = y.Class("baseLoginAction", {
                "extend": i,
                "construct": function(e) {
                    this.panel = e.panel,
                    this.types = e.types,
                    this.toastPanel = e.toastPanel,
                    this.verifyCenter = e.verifyCenter,
                    this.isPca = "pca" == e.business,
                    this.errMsg = e.errMsg,
                    this.doms = {},
                    this.nameKit = null,
                    this.areaIns = null,
                    this.rpage = "passsdk",
                    this.block = "psprt_acc",
                    this.isFirstShow = !0
                },
                "methods": {
                    "init": function() {
                        this.render(),
                        this.bindEvent()
                    },
                    "bindEvent": function() {
                        this.initArea(),
                        this.toggleEye(),
                        this.handlePwdInput(),
                        this.initNameInput(),
                        this.initMailSuggest(),
                        this.handleBtn(),
                        this.handleAutoLogin(),
                        this.errMsg && this.nameKit.showErrMsg(this.errMsg)
                    },
                    "render": function() {
                        var e = JSON.parse(y.cookie.get("QC160") || "{}")
                          , e = this.renderHtml(s, {
                            "noSmsLogin": this.types.indexOf(3) < 0,
                            "noReg": this.types.indexOf(5) < 0,
                            "isPca": this.isPca,
                            "autoLogin": 0 != e.autoLogin
                        });
                        this.panel.innerHTML = e,
                        this.doms = {
                            "loginBtn": this.panel.querySelector('[data-baseLogin="loginBtn"]'),
                            "areaPanel": this.panel.querySelector('[data-baseLogin="area"]'),
                            "nameErr": this.panel.querySelector('[data-baseLogin="nameErr"]'),
                            "nameInput": this.panel.querySelector('[data-baseLogin="nameInput"]'),
                            "pwdInput": this.panel.querySelector('[data-baseLogin="pwdInput"]'),
                            "pwdErr": this.panel.querySelector('[data-baseLogin="pwdErr"]'),
                            "pwdEye": this.panel.querySelector('[data-baseLogin="pwdEye"]'),
                            "smsLogin": this.panel.querySelector('[data-baseLogin="smsLogin"]'),
                            "reg": this.panel.querySelector('[data-baseLogin="reg"]'),
                            "mailSuggestPanel": this.panel.querySelector('[data-baseLogin="mailSuggest"]'),
                            "autologin": this.panel.querySelector('[data-baseLogin="autologin"]')
                        }
                    },
                    "showPanel": function(e) {
                        this.show(e || this.panel)
                    },
                    "initArea": function() {
                        this.areaIns = new o({
                            "panel": this.doms.areaPanel,
                            "fireName": f
                        }),
                        this.areaIns.render()
                    },
                    "toggleEye": function() {
                        var t = this.doms.pwdEye
                          , n = this.doms.pwdInput;
                        r.on(t, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            d.hasClass(t, "icon-eyes-close") ? (d.addClass(t, "icon-eyes-open"),
                            d.removeClass(t, "icon-eyes-close"),
                            n.setAttribute("type", "text")) : (d.addClass(t, "icon-eyes-close"),
                            d.removeClass(t, "icon-eyes-open"),
                            n.setAttribute("type", "password"))
                        })
                    },
                    "handlePwdInput": function() {
                        var t = this
                          , n = this.doms.pwdInput;
                        r.on(n, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.hidePwdErr()
                        });
                        r.on(n, "blur", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            0 == n.value.trim().length && (n.value = "")
                        });
                        var e = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.hidePwdErr(),
                            t.setBaseLoginBtnStatus()
                        };
                        r.on(n, "keyup", e),
                        r.on(n, "input", e)
                    },
                    "setBaseLoginBtnStatus": function() {
                        var e = this.nameKit.checkNameValidate()
                          , t = 0 < this.doms.pwdInput.value.trim().length
                          , n = this.doms.loginBtn;
                        e && t ? d.removeClass(n, "btn-gray") : d.addClass(n, "btn-gray")
                    },
                    "showPwdErr": function(e) {
                        this.doms.pwdErr.innerHTML = e,
                        d.removeClass(this.doms.pwdErr, "dn")
                    },
                    "hidePwdErr": function() {
                        d.addClass(this.doms.pwdErr, "dn")
                    },
                    "initNameInput": function() {
                        var e = this;
                        this.nameKit = new l({
                            "name": this.doms.nameInput,
                            "nameErr": this.doms.nameErr,
                            "mailPanel": this.doms.mailSuggestPanel,
                            "zoneKey": this.acode,
                            "fireEnableName": m,
                            "zoneChangeFireName": f
                        }),
                        this.nameKit.init(),
                        c.on(m, function() {
                            e.setBaseLoginBtnStatus()
                        })
                    },
                    "initMailSuggest": function() {
                        new g({
                            "panel": this.doms.mailSuggestPanel,
                            "input": this.doms.nameInput,
                            "prompt": !1
                        }).init()
                    },
                    "handleBtn": function() {
                        var t = this
                          , n = this.doms.loginBtn;
                        r.on(n, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            !d.hasClass(n, "btn-gray") && p.isAgree() && (u.click({
                                "rpage": t.rpage,
                                "block": t.block,
                                "rseat": "acc_login"
                            }),
                            t.doLogin())
                        });
                        r.on(this.doms.smsLogin, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            u.click({
                                "rpage": t.rpage,
                                "block": t.block,
                                "rseat": "acc2sms"
                            }),
                            c.fire({
                                "type": "toggleLoginTypes",
                                "data": {
                                    "type": 3
                                }
                            })
                        });
                        r.on(this.doms.reg, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            c.fire({
                                "type": "toggleLoginTypes",
                                "data": {
                                    "type": 4
                                }
                            })
                        })
                    },
                    "handleAutoLogin": function() {
                        var t;
                        this.isPca && (t = this.doms.autologin,
                        r.on(t, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            d.hasClass(t, "selected") ? d.removeClass(t, "selected") : d.addClass(t, "selected")
                        }))
                    },
                    "doLogin": function(e) {
                        var o = this
                          , s = {
                            "passwd": o.doms.pwdInput.value,
                            "acode": o.areaIns.getAcode().acode,
                            "phone": o.doms.nameInput.value,
                            "token": e
                        };
                        a.login(s, function(e) {
                            o.nameKit.clearErrMsg();
                            var t, n, i = e.msg;
                            "A00000" == e.code && e.data ? ((t = e.data).rpage = v,
                            c.fire({
                                "type": "handleLoginSuc",
                                "data": t
                            })) : "P00223" == e.code ? ((n = s).ErrCb = function() {
                                o.nameKit.showPhoneMsg("请稍后重试"),
                                window.MITO && window.MITO.log({
                                    "message": "账号密码登录：触发验证中心失败",
                                    "data": {
                                        "acode": s.acode,
                                        "phone": s.phone
                                    }
                                })
                            }
                            ,
                            o.verifyCenter.callSDK(e, n, function(e) {
                                e ? o.doLogin(e) : o.nameKit.showPhoneMsg("请稍后重试")
                            })) : "P00807" == e.code ? c.fire({
                                "type": "toggleLoginTypes",
                                "data": {
                                    "type": 5,
                                    "rpage": v
                                }
                            }) : "P00159" === e.code || "P00908" == e.code ? (n = "P00159" === e.code ? "hrisk" : "lock",
                            c.fire({
                                "type": "showQrCodeLogin",
                                "data": {
                                    "type": n,
                                    "mobile": i
                                }
                            }),
                            d.addClass(o.panel, "dn")) : "P00119" == e.code && 0 <= i.indexOf("再错") || "P00125" == e.code || "P00141" == e.code ? h.showTip(o.toastPanel, {
                                "tip": i,
                                "btnTip": "确定"
                            }) : o.nameKit.showErrMsg(i)
                        })
                    },
                    "resetAcode": function(e, t) {
                        this.areaIns.resetAcode(e, t)
                    },
                    "getAutoLoginStatus": function() {
                        return d.hasClass(this.doms.autologin, "selected")
                    }
                }
            })
        }
        .call(n, b, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, b(0))
}
, function(t, n, r) {
    (function(a) {
        var e = function(e, t, n) {
            var i = r(7)
              , o = r(5)
              , s = r(2);
            n.exports = a.Class("areaListService", {
                "construct": function() {
                    this._remoteInterface = new i({
                        "getAreacodeIf": {
                            "url": o.getAreacode
                        }
                    })
                },
                "methods": {
                    "getAreacode": function(t) {
                        var e = s.getConfig();
                        this._remoteInterface.send({
                            "ifname": "getAreacodeIf",
                            "param": {
                                "agenttype": e.agenttype,
                                "app_version": e.appVersion || "",
                                "fromSDK": e.fromSDK,
                                "local": 1,
                                "ptid": e.ptid,
                                "sdk_version": e.sdk_version
                            }
                        }, function(e) {
                            t && t(e)
                        })
                    }
                }
            })
        }
        .call(n, r, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, r(0))
}
, function(t, n, d) {
    "use strict";
    (function(a) {
        var e = function(e, t, n) {
            var r = d(1)
              , c = d(25)
              , i = "__IFRAME__"
              , o = function() {}
              , s = a.Class("FormRequest", {
                "construct": function(e) {
                    e = e || {},
                    this.form = e.form || {},
                    this.data = e.data || [],
                    this.iframe = e.iframe || {},
                    this.callbackName = e.callbackName || "__CALLBACK__" + Math.floor(2147483648 * Math.random()).toString(36),
                    this.randomCb = !e.callbackName,
                    this.callback = e.callback || o,
                    this.needIframe = !1 !== e.needIframe && !0 !== e.needIframe || e.needIframe,
                    this.needDestroy = e.needDestroy || !1,
                    this.noTranslateKeys = e.noTranslateKeys || [],
                    this.needMd5 = e.needMd5 || !1,
                    this.init()
                },
                "methods": {
                    "init": function() {
                        i += Math.floor(2147483648 * Math.random()).toString(36),
                        this.form = this._dealForm(this.form),
                        this.formElem = this._createForm(this.form),
                        this._importData(this.formElem, this.data),
                        this.needIframe && (this.iframe = this._dealIframe(this.iframe),
                        this.iframeElem = this._createIframe(this.iframe))
                    },
                    "_translateStr": function(e, t) {
                        if ((e = e || "") && "string" == typeof e && e.length)
                            for (var n = [{
                                "origin": '"',
                                "dest": "&quot;"
                            }, {
                                "origin": "<",
                                "dest": "&lt;"
                            }, {
                                "origin": ">",
                                "dest": "&gt;"
                            }, {
                                "origin": "\\\\",
                                "dest": "&#92;"
                            }, {
                                "origin": "&",
                                "dest": "&amp;"
                            }], i = 0; i < n.length; i++) {
                                var o, s = n[i].origin;
                                "&" === s && t || (o = new RegExp(s,"g"),
                                s = n[i].dest,
                                e = e.replace(o, s))
                            }
                        return e
                    },
                    "_dealForm": function(e) {
                        return 1 != (e = e || {}).nodeType && (e["accept-charset"] = e["accept-charset"] || "utf-8",
                        e["action"] = e["action"] || "",
                        e["enctype"] = e["enctype"] || "application/x-www-form-urlencoded",
                        e["method"] = e["method"] || "post",
                        e["name"] = e["name"] || "__FORM__",
                        e["target"] = e["target"] || i,
                        e["style"] = e["style"] || "display:none;"),
                        e
                    },
                    "_createForm": function(e) {
                        if (1 == (e = e || {}).nodeType)
                            return e;
                        var t = null
                          , n = r.getElementByAttr("form", "name", e.name);
                        if (0 < n.length)
                            t = n[0],
                            r.removeAllChild(t);
                        else {
                            for (var i in t = document.createElement("form"),
                            e)
                                e[i] && t.setAttribute(i, e[i]);
                            document.body.appendChild(t)
                        }
                        return t
                    },
                    "_dealIframe": function(e) {
                        return 1 != (e = e || {}).nodeType && (e.style = e.style || "display:none;",
                        e.name = e.name || i),
                        e
                    },
                    "_createIframe": function(e) {
                        if (1 == (e = e || {}).nodeType)
                            return e;
                        var t = e.name || ""
                          , n = (e.style,
                        r.getElementByAttr("iframe", "name", t))
                          , t = null;
                        return 0 < n.length ? t = n[0] : ((n = document.createElement("div")).innerHTML = '<iframe style="display:none;" name="' + e.name + '"></iframe>',
                        n.setAttribute("style", "display:none"),
                        t = n,
                        document.body.appendChild(n)),
                        t
                    },
                    "_importData": function(e, t) {
                        if (this.formElem) {
                            r.isEmptyObject(t) || r.isArray(t) || (this.randomCb && (t.callback = "window.parent." + this.callbackName),
                            t = this.sortData(t));
                            for (var n = 0; n < t.length; n++) {
                                var i, o = this._translateStr(String(t[n].name)), s = String(t[n].value), s = 0 <= this.noTranslateKeys.indexOf(o) ? this._translateStr(s, !0) : this._translateStr(s), a = String(t[n].type || "text");
                                o && (0 < (i = r.getElementByAttr("input", "name", o, e)).length ? i[0].setAttribute("name", s) : ((i = document.createElement("input")).name = o,
                                i.value = s,
                                i.type = a,
                                e.appendChild(i)))
                            }
                            return !0
                        }
                    },
                    "submit": function() {
                        if (this.formElem)
                            try {
                                var t;
                                this.needIframe && (this.needDestroy && this.callback ? (t = this,
                                window[this.callbackName] = function(e) {
                                    t.callback(e),
                                    t.iframeElem && (t.iframeElem.parentNode.removeChild(t.iframeElem),
                                    t.iframeElem = null),
                                    t.randomCb && (window[t.callbackName] = null)
                                }
                                ) : window[this.callbackName] = this.callback),
                                this.formElem.submit(),
                                this.needDestroy && (this.formElem.parentNode.removeChild(this.formElem),
                                this.formElem = null)
                            } catch (e) {
                                this.callback && this.callback({
                                    "code": "E0000F",
                                    "msg": "表单出错！",
                                    "data": e
                                })
                            }
                    },
                    "reset": function() {
                        this.formElem && this.formElem.reset()
                    },
                    "sortData": function(e) {
                        var t, n = [];
                        for (t in e) {
                            var i = {
                                "name": t,
                                "value": e[t],
                                "type": "text"
                            };
                            n.push(i)
                        }
                        if (this.needMd5) {
                            n.sort(function(e, t) {
                                return e.name < t.name ? -1 : e.name > t.name ? 1 : 0
                            });
                            for (var o = {}, s = 0; s < n.length; s++)
                                o[n[s].name] = n[s].value;
                            var a = c(o);
                            n.push({
                                "name": "qd_sc",
                                "value": a,
                                "type": "text"
                            })
                        }
                        return n
                    }
                }
            });
            n.exports = s
        }
        .call(n, d, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, d(0))
}
, function(e, t, o) {
    "use strict";
    t = function(e, t, n) {
        var v = o(1)
          , i = {
            "request": function(e, t) {
                var o, n, s, i = (t = t || {}).data || "", a = !1 !== t.async, r = t.username || "", c = t.password || "", d = (t.method || "GET").toUpperCase(), l = t.headers || {}, u = t.timeout || 2e3, p = {}, h = t.withCredentials || !1;
                function g() {
                    if (4 == s.readyState) {
                        var e;
                        try {
                            e = s.status
                        } catch (t) {
                            return void f("failure")
                        }
                        f(e),
                        f(200 <= e && e < 300 || 304 == e || 1223 == e || 0 === e ? "success" : "failure"),
                        window.setTimeout(function() {
                            s && (s.onreadystatechange = function() {}
                            ),
                            a && (s = null)
                        }, 0)
                    }
                }
                function f(e) {
                    var t, n = p[e = "on" + e];
                    if (n) {
                        o && window.clearTimeout(o);
                        try {
                            t = s.responseText || "{}",
                            n(JSON.parse(t))
                        } catch (i) {
                            return n("")
                        }
                        return 1
                    }
                }
                for (n in t)
                    p[n] = t[n];
                try {
                    for (n in s = function() {
                        if (window.XMLHttpRequest)
                            return new XMLHttpRequest;
                        if (window.ActiveXObject)
                            try {
                                return new window.ActiveXObject("Msxml2.XMLHTTP")
                            } catch (e) {
                                try {
                                    return new window.ActiveXObject("Microsoft.XMLHTTP")
                                } catch (t) {}
                            }
                    }(),
                    "[object Object]" == Object.prototype.toString.call(i) && (i = v.jsonToQuery(i)),
                    "GET" == d && (i && (e += (0 <= e.indexOf("?") ? "&" : "?") + i,
                    i = null),
                    t["noCache"] && (e += (0 <= e.indexOf("?") ? "&" : "?") + "b" + +new Date + "=1")),
                    r ? s.open(d, e, a, r, c) : s.open(d, e, a),
                    a && (s.onreadystatechange = g),
                    "POST" == d && s.setRequestHeader("Content-Type", l["Content-Type"] || "application/x-www-form-urlencoded"),
                    l)
                        l.hasOwnProperty(n) && s.setRequestHeader(n, l[n]);
                    "withCredentials"in s && (s.withCredentials = h),
                    f("beforerequest"),
                    u && (o = setTimeout(function() {
                        s.onreadystatechange = function() {}
                        ,
                        s.abort(),
                        f("timeout") || f("failure")
                    }, u)),
                    s.send(i),
                    a || g()
                } catch (m) {
                    f("failure")
                }
                return s
            }
        };
        n.exports = i
    }
    .call(t, o, t, e);
    t === undefined || (e.exports = t)
}
, function(e, t) {
    e.exports = '{{if type == \'suc\'}} <div class="qy-cover-align"> <div class="cover-content"> <div class="qy-result-success"> <div class="success-title"> <i class="iconfont icon-success"></i> <span class="title-txt">{{title}}</span> </div> {{if tip}} <div class="success-tips">{{tip}}</div> {{/if}} <div class="qyl-success-info"> {{if icon}} <img class="user-avatar" src="{{icon}}"> {{/if}} {{if nickname}} <div class="login-user-name">{{nickname}}</div> {{/if}} </div> </div> </div> </div> {{else if type == \'toast\'}} <div class="qy-cover-align"> <div class="cover-content"> <div class="qy-login-warning"> <i class="iconfont icon-warning"></i> <div class="warning-title">{{tip}}</div> </div> </div> </div> {{else}} <div class="qy-cover-align"> <div class="cover-content"> <div class="qy-login-warning"> <i class="iconfont icon-warning"></i> <div class="warning-title">{{tip}}</div> <div class="qy-login-btn"> <div class="btn-common"> <div class="btn-inner btn-major" data-toast="btn">{{btnTip}}</div> </div> </div> </div> </div> </div> {{/if}}'
}
, function(e, t) {
    e.exports = '<div class="country-code" data-area="panel"> <span class="country-current" data-area="show">中国大陆 +86</span> <i class="iconfont icon-arr"></i> <span class="splite-line"></span> </div> <div class="country-code-list dn" data-area="listPanel"> <ul> {{each lists as item}} <li data-area-acode="{{item.acode}}" data-area-name="{{item.name}}" class="{{item.selected}}">{{item.name}} +{{item.acode}}</li> {{/each}} </ul> </div>'
}
, function(e, t) {
    e.exports = '<div class="qy-login-tab {{if noSmsLogin == true}}single-tab{{/if}}"> <a href="javascript:;" class="selected">密码登录<span class="tab-line"></span></a> <a href="javascript:;" data-baseLogin="smsLogin" class="{{if noSmsLogin == true}}dn{{/if}}">短信登录</a> </div> <div class="qy-login-field"> <div class="field-item"> <div class="field-error dn" data-baseLogin="nameErr">请输入手机号/邮箱</div> <div class="field-country-code" data-baseLogin="area"></div> <div class="field-account"> <input type="text" class="input-box" data-baseLogin="nameInput" maxlength="40" placeholder="请输入手机号/邮箱"/> <div class="account-dropList dn" data-baseLogin="mailSuggest"></div> </div> </div> <div class="field-item"> <div class="field-error dn" data-baseLogin="pwdErr">账号或密码错误</div> <div class="field-confirm-code"> <input type="password" class="input-box" data-baseLogin="pwdInput" maxlength="20" placeholder="请输入密码"/> <i class="iconfont icon-eyes-close" data-baseLogin="pwdEye"></i> </div> </div> <div class="field-other"> {{if isPca == true}} <div class="other-status"> <a href="javascript:;" class="status-item {{if autoLogin == true}}selected{{/if}}" data-baselogin="autologin"> <span class="iconfont icon-select"></span>自动登录 </a> </div> {{/if}} <div class="other-register"> <a href="javascript:;" class="register-account {{if noReg == true}}dn{{/if}}" data-baseLogin="reg">注册账号</a> </div> <div class="other-forget"> <a href="https://www.iqiyi.com/safety/findPassword.html" class="forget-pwd" target="_blank">忘记密码？</a> </div> </div> </div> <div class="qy-login-btn"> <div class="btn-common"> <div class="btn-inner btn-major btn-gray" data-baseLogin="loginBtn"> 登录 </div> </div> </div>'
}
, function(t, n, s) {
    (function(l) {
        var e = function(e, t, n) {
            var i = s(7)
              , a = s(16)
              , r = s(10)
              , o = s(5)
              , c = s(2)
              , d = s(1);
            n.exports = l.Class("baseLoginService", {
                "construct": function() {
                    this._remoteInterface = new i({
                        "login": {
                            "url": o.login
                        }
                    })
                },
                "methods": {
                    "login": function(e, t) {
                        var n = c.getConfig()
                          , i = this
                          , o = a.rsaFun(e.passwd)
                          , s = {
                            "__NEW": 1,
                            "agenttype": n.agenttype,
                            "app_version": n.appVersion || "",
                            "area_code": e.acode,
                            "checkExist": 1,
                            "dfp": "",
                            "email": e.phone
                        };
                        e.token && (s.env_token = e.token),
                        s = l.extend(s, {
                            "fromSDK": n.fromSDK,
                            "lang": "",
                            "nr": 2,
                            "passwd": o,
                            "ptid": n.ptid,
                            "sdk_version": n.sdk_version,
                            "verifyPhone": 1
                        }),
                        r.getDFP(function(e) {
                            s.dfp = e,
                            d.isCors() && (s.qd_sc = l.md5(decodeURIComponent(d.jsonToQuery(s)) + "tS7BdPLU2w0JD89dh")),
                            i._remoteInterface.send({
                                "ifname": "login",
                                "param": s
                            }, function(e) {
                                t && t(e)
                            })
                        })
                    }
                }
            })
        }
        .call(n, s, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, s(0))
}
, function(t, n, d) {
    (function(c) {
        var e = function(e, t, n) {
            var i = d(6)
              , o = d(57)
              , a = d(1)
              , s = d(13)
              , r = d(3);
            n.exports = c.Class("mailSuggest", {
                "extend": i,
                "construct": function(e) {
                    this.panel = e.panel,
                    this._input = e.input,
                    this._curStr = "",
                    this.pattern = e.pattern || /^[0-9a-zA-Z_][-_\.0-9a-zA-Z-]{1,}@([0-9a-zA-Z][0-9a-zA-Z-])*/,
                    this._mails = e.mails || ["qq.com", "163.com", "126.com", "sina.com", "sina.cn", "hotmail.com", "gmail.com", "yahoo.cn", "139.com"],
                    this._max = e.max || 3
                },
                "methods": {
                    "init": function() {
                        if (this.panel && this._input)
                            return this.bindEvent(),
                            this
                    },
                    "render": function(e) {
                        e = this.renderHtml(o, {
                            "data": e
                        });
                        this.panel.innerHTML = e,
                        this.handleItem()
                    },
                    "bindEvent": function() {
                        var n = this
                          , i = {
                            "13": "enter",
                            "27": "esc",
                            "37": "left",
                            "38": "up",
                            "39": "right",
                            "40": "down",
                            "9": "tab"
                        };
                        a.on(n._input, "keydown", function(e) {
                            e.stopPropagation && e.stopPropagation();
                            var t = e.keyCode + "";
                            t in i ? "38" == t || "40" == t ? ("38" == t && e.preventDefault(),
                            n.changeSuggest(i[t])) : "13" == t && n.enterSuggest() : setTimeout(function() {
                                n.useCorrectSuggest()
                            }, 50)
                        });
                        a.on(n._input, "focus", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            n._input.value && n.useCorrectSuggest()
                        })
                    },
                    "handleItem": function() {
                        var s = this
                          , e = this.panel.querySelectorAll('[data-maisuggest="item"]');
                        this.itemClk = function(e) {
                            e.stopPropagation && e.stopPropagation();
                            var t = (e = e || window.event).target || e.srcElement
                              , e = t.getAttribute("data-index")
                              , e = parseInt(e, 10)
                              , t = t.innerHTML;
                            s._input.value = t,
                            s.hidePanel()
                        }
                        ,
                        this.itemMouseOver = function(e) {
                            e.stopPropagation && e.stopPropagation();
                            for (var t = (e = e || window.event).target || e.srcElement, n = t.getAttribute("data-index"), n = parseInt(n, 10), i = s.suggests, o = 0; o < i.length; o++)
                                o !== n ? r.removeClass(t, "selected") : (r.addClass(t, "selected"),
                                s._input.value = t.innerHTML)
                        }
                        ;
                        for (var t, n = 0; n < e.length; n++)
                            t = n,
                            a.on(e[t], "click", s.itemClk),
                            a.on(e[t], "mouseover", s.itemMouseOver)
                    },
                    "unBindEvent": function() {
                        for (var t = this.panel.querySelectorAll('[data-maisuggest="item"]'), e = 0; e < t.length; e++)
                            !function(e) {
                                a.un(t[e], "click", this.itemClk),
                                a.un(t[e], "click", this.itemMouseOver)
                            }(e);
                        this.itemClk = null,
                        this.itemMouseOver = null
                    },
                    "useCorrectSuggest": function() {
                        var e = this
                          , t = e._input.value || "";
                        e._curStr = s.trimAllBlank(t);
                        t = e.assemble(e.parseMail());
                        e._curStr && 0 < t.length && (!e.pattern || e.pattern && e.pattern.test(e._curStr)) ? (e.render(t),
                        e.suggests = e.panel.querySelectorAll('[data-maisuggest="item"]'),
                        e.show(e.panel)) : e.hidePanel()
                    },
                    "hidePanel": function() {
                        this.unBindEvent(),
                        this.hide(this.panel)
                    },
                    "changeSuggest": function(e) {
                        for (var t = this.suggests, n = t.length, i = 0, o = 1, i = "up" == e ? -1 : 1, s = 0; s < n; s++)
                            if (r.hasClass(t[s], "selected")) {
                                o = parseInt(t[s].getAttribute("data-index"), 10);
                                break
                            }
                        n - 1 <= (o = (o += i) <= 0 ? 0 : o) && (o = n - 1);
                        for (s = 0; s < n; s++)
                            parseInt(t[s].getAttribute("data-index"), 10) == o ? (r.addClass(t[s], "selected"),
                            this._input.value = t[s].innerHTML) : r.removeClass(t[s], "selected")
                    },
                    "enterSuggest": function() {
                        if (!r.hasClass(this.panel, "dn"))
                            for (var e = this.suggests, t = 0; t < e.length; t++)
                                r.hasClass(e[t], "selected") && (this._input.value = e[t].innerHTML,
                                this.hidePanel())
                    },
                    "parseMail": function() {
                        var e = this._mails.concat()
                          , t = this._curStr.match(/(@)(.*)/);
                        return t && t[2] && (e = e.filter(function(e) {
                            return -1 < e.indexOf(t[2])
                        })),
                        this._max && e.length > this._max && (e.length = this._max),
                        e
                    },
                    "assemble": function(e) {
                        var e = e
                          , n = this._curStr.replace(/@.*/, "");
                        return e.length && (e = e.map(function(e, t) {
                            return {
                                "mail": n + "@" + e
                            }
                        })).forEach(function(e, t) {
                            e.index = t
                        }),
                        e
                    }
                }
            })
        }
        .call(n, d, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, d(0))
}
, function(e, t) {
    e.exports = '<ul> {{each data as item}} <li> <a href="javascript:;" class="dropList-item" data-maisuggest="item" data-index="{{item.index}}">{{item.mail}}</a> </li> {{/each}} </ul>'
}
, function(t, n, p) {
    (function(u) {
        var e = function(e, t, n) {
            var i = p(6)
              , o = p(59)
              , a = new (p(60))
              , s = p(1)
              , r = p(4)
              , c = p(8)
              , d = p(3)
              , l = p(9);
            n.exports = u.Class("scanLoginAction", {
                "extend": i,
                "construct": function(e) {
                    this.panel = e.panel,
                    this.type = e.type || "normal",
                    this.msg = e.msg || "",
                    this.appTitle = e.appTitle || "爱奇艺手机APP",
                    this.business = e.business,
                    this._pullInterval = 2e3,
                    this.doms = {},
                    this.hidden = !0,
                    this.reGenClick = null,
                    this.backClick = null,
                    this.smsLogincli = null,
                    this.rpage = "normal" == this.type ? "passsdk" : "lock" == this.type ? "device_locked" : "device_new",
                    this.block = "normal" == this.type ? "psprt_QRcode" : ""
                },
                "methods": {
                    "init": function() {
                        this.reGenClick && this.unBindEvent(),
                        this.render(),
                        this.bindEvent()
                    },
                    "bindEvent": function() {
                        var t = this;
                        this.reGenClick = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.refreshQrcode()
                        }
                        ,
                        s.on(this.doms.reGenBtn, "click", this.reGenClick),
                        "normal" != this.type && (this.backClick = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.hidePanel(),
                            r.fire({
                                "type": "backShow",
                                "data": {
                                    "resetShowPanel": !0
                                }
                            })
                        }
                        ,
                        s.on(this.doms.back, "click", this.backClick),
                        this.smsLogincli = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.hidePanel(),
                            r.fire({
                                "type": "toggleLoginTypes",
                                "data": {
                                    "type": 3
                                }
                            })
                        }
                        ,
                        s.on(this.doms.smsLogin, "click", this.smsLogincli))
                    },
                    "unBindEvent": function() {
                        s.un(this.doms.reGenBtn, "click", this.reGenClick),
                        this.reGenClick = null,
                        this.doms.back && (s.un(this.doms.back, "click", this.backClick),
                        this.backClick = null,
                        s.un(this.doms.smsLogin, "click", this.smsLogincli),
                        this.smsLogincli = null)
                    },
                    "render": function() {
                        var e = this.renderHtml(o, {
                            "type": this.type || "normal",
                            "msg": this.msg || "",
                            "appTitle": this.appTitle
                        });
                        this.panel.innerHTML = e,
                        this.doms = {
                            "code": this.panel.querySelector('[data-scanLogin="code"]'),
                            "codeFailPanel": this.panel.querySelector('[data-scanLogin="codeFailPanel"]'),
                            "codeSuc": this.panel.querySelector('[data-scanLogin="codeSucPanel"]'),
                            "codeImg": this.panel.querySelector('[data-scanLogin="codeImg"]'),
                            "reGenBtn": this.panel.querySelector('[data-scanLogin="reGen"]'),
                            "back": this.panel.querySelector('[data-scanLogin="back"]'),
                            "smsLogin": this.panel.querySelector('[data-scanLogin="smsLogin"]')
                        },
                        this.scsSend = !1
                    },
                    "showPanel": function(e) {
                        type = e.type || "normal",
                        e.type !== this.type && (this.type = e.type,
                        this.rpage = "normal" == this.type ? "passsdk" : "lock" == this.type ? "device_locked" : "device_new",
                        this.block = "normal" == this.type ? "psprt_QRcode" : "",
                        this.msg = e.msg,
                        this.init()),
                        this.hidden = !1,
                        this.show(this.panel),
                        this.refreshQrcode()
                    },
                    "hidePanel": function() {
                        this.hidden = !0,
                        clearTimeout(this._pollTokenLoginTimer),
                        clearTimeout(this._arcodeOnerrorTimer),
                        this.hide(this.panel)
                    },
                    "refreshQrcode": function() {
                        var i = this;
                        i.hiden || a.genLoginToken(function(e) {
                            var t, n;
                            "A00000" === e.code ? (i._loginToken = e.data.token,
                            i._loginTokenExpire = e.data.expire,
                            t = a.getQrCode(e.data.url) + "&_=" + Math.random(),
                            n = i.doms.codeImg,
                            i._arcodeOnerrorTimer = null,
                            n.onload = function() {
                                n.onload = n.onerror = function() {}
                                ,
                                clearTimeout(i._arcodeOnerrorTimer),
                                i.qrcodeImgSrcChanged()
                            }
                            ,
                            n.onerror = function() {
                                n.onload = n.onerror = function() {}
                                ,
                                clearTimeout(i._arcodeOnerrorTimer),
                                d.removeClass(i.doms.codeFailPanel, "dn"),
                                i.hide(i.doms.codeSuc),
                                "pca" == i.business && l.callPca()
                            }
                            ,
                            i._arcodeOnerrorTimer = setTimeout(function() {
                                n.onerror()
                            }, 5e3),
                            n.src = t) : (d.removeClass(i.doms.codeFailPanel, "dn"),
                            i.hide(i.doms.codeSuc),
                            window.MITO && window.MITO.log({
                                "message": "扫码登录：刷新二维码接口gen_login_token.action失败",
                                "data": e
                            }))
                        })
                    },
                    "qrcodeImgSrcChanged": function() {
                        var n = this
                          , i = 30;
                        n.hide(n.doms.codeFailPanel),
                        n.hide(n.doms.codeSuc),
                        d.removeClass(n.doms.code, "dn");
                        var o = !1;
                        n._pollTokenLoginTimer = setTimeout(function s() {
                            a.checkTokenLogin(n._loginToken, function(e) {
                                var t;
                                "A00000" === e.code ? (t = {},
                                (t = e.data && e.data.userinfo ? e.data.userinfo : t).rpage = "login_scs_QR",
                                r.fire({
                                    "type": "handleLoginSuc",
                                    "data": t
                                })) : (clearTimeout(n._pollTokenLoginTimer),
                                o || n.hidden || (0 < i ? (n._pollTokenLoginTimer = setTimeout(s, 1e3),
                                0 == --i ? (n.hide(n.doms.codeSuc),
                                d.removeClass(n.doms.code, "dn"),
                                d.removeClass(n.doms.codeFailPanel, "dn")) : "P01006" === e.code ? (n.hide(n.doms.code),
                                d.removeClass(n.doms.codeSuc, "dn"),
                                n.scsSend || (c.block({
                                    "rpage": n.rpage,
                                    "block": "QRscan_scs"
                                }),
                                n.scsSend = !0)) : "P01007" === e.code && (clearTimeout(n._pollTokenLoginTimer),
                                n.hide(n.doms.codeSuc),
                                d.removeClass(n.doms.code, "dn"),
                                n.refreshQrcode(),
                                n.scsSend = !1)) : (d.removeClass(n.doms.code, "dn"),
                                d.removeClass(n.doms.codeFailPanel, "dn"),
                                n.hide(n.doms.codeSuc))))
                            })
                        }, n._pullInterval),
                        clearTimeout(n._loginTokenExpireTimer),
                        n._loginTokenExpireTimer = null,
                        n._loginTokenExpireTimer = setTimeout(function() {
                            o = !0,
                            clearTimeout(n._pollTokenLoginTimer),
                            n._pollTokenLoginTimer = null,
                            clearTimeout(n._loginTokenExpireTimer),
                            n._loginTokenExpireTimer = null,
                            n.hidden || n.refreshQrcode()
                        }, 1e3 * n._loginTokenExpire)
                    },
                    "destroy": function() {
                        clearTimeout(this._pollTokenLoginTimer)
                    }
                }
            })
        }
        .call(n, p, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, p(0))
}
, function(e, t) {
    e.exports = '<div class="qy-login-title"> {{if type != \'normal\'}} <span class="back-link" data-scanLogin="back"> <i class="iconfont icon-back"></i>返回 </span> {{/if}} <div class="title-content"> {{if type == \'normal\'}} <div class="major-desc"> <p>打开<span class="theme-color">{{appTitle}}</span></p> <p>扫描二维码登录</p> </div> {{else if type == \'lock\'}} <div class="major-desc"> <p>已开启设备锁</p> </div> <div class="minor-desc"> <p>{{msg}}</p> </div> {{else if type == \'hrisk\'}} <div class="title-content"> <div class="major-desc"> <p>当前登录存在风险</p> </div> <div class="minor-desc"> <p>为了账号安全，请在手机上打开爱奇艺APP，<br/>扫描二维码登录</p> </div> </div> {{/if}} </div> </div> <div class="qy-login-qrcode" data-scanLogin="code"> <div class="qrcode-pic"> <img data-scanLogin="codeImg"> </div> <div class="qrcode-cover dn" data-scanLogin="codeFailPanel"> <div class="qrcode-cover-middle"> <div class="cover-desc">二维码已失效</div> <div class="cover-refresh" data-scanLogin="reGen"> <i class="iconfont icon-refresh"></i>点击刷新</div> </div> </div> </div> <div class="qy-login-saoma-success dn" data-scanLogin="codeSucPanel"> <div class="saoma-con"> <i class="iconfont icon-success"></i> <div class="saoma-title">扫码成功</div> <div class="saoma-tips">请在手机上确认 [ 授权登录 ]</div> </div> </div> {{if type != \'normal\'}} <div class="qy-login-problem"> <div class="problem-ask"> {{if type == \'lock\'}} <span class="ask-desc">主设备手机不在身边</span> {{else}} <span class="ask-desc">没有安装爱奇艺APP</span> {{/if}} <i class="iconfont icon-ask"> <span class="pop-arr"></span> <div class="problem-pop">建议安装爱奇艺APP，扫码登录更安全，有效防止盗号。不想安装？可以使用<a href="javascript:;" class="theme-color" data-scanLogin="smsLogin">短信登录</a> </div> </i> </div> </div> {{/if}}'
}
, function(t, n, a) {
    (function(r) {
        var e = function(e, t, n) {
            var i = a(7)
              , o = a(5)
              , s = a(2);
            n.exports = r.Class("scanLoginService", {
                "construct": function() {
                    this._remoteInterface = new i({
                        "genLoginTokenIf": {
                            "url": o.genLoginToken
                        },
                        "checkTokenLoginIf": {
                            "url": o.isTokenLogin
                        }
                    })
                },
                "methods": {
                    "genLoginToken": function(t) {
                        var e = s.getConfig();
                        this._remoteInterface.send({
                            "ifname": "genLoginTokenIf",
                            "param": {
                                "agenttype": e.agenttype,
                                "app_version": e.appVersion || "",
                                "device_name": "网页端",
                                "fromSDK": e.fromSDK,
                                "ptid": e.ptid,
                                "sdk_version": e.sdk_version,
                                "surl": 1
                            }
                        }, function(e) {
                            t && t(e)
                        })
                    },
                    "checkTokenLogin": function(e, t) {
                        var n = s.getConfig();
                        this._remoteInterface.send({
                            "ifname": "checkTokenLoginIf",
                            "param": {
                                "agenttype": n.agenttype,
                                "app_version": n.appVersion || "",
                                "fromSDK": n.fromSDK,
                                "ptid": n.ptid,
                                "sdk_version": n.sdk_version,
                                "token": e
                            }
                        }, function(e) {
                            t && t(e)
                        })
                    },
                    "getQrCode": function(e) {
                        for (var t = encodeURIComponent(e), n = [{
                            "key": "!",
                            "value": "%21"
                        }], i = 0, o = n.length; i < o; i++)
                            var s = new RegExp(n[i]["key"],"g")
                              , t = t.replace(s, n[i]["value"]);
                        var a = "35f4223bb8f6c8638dc91d94e9b16f5" + t
                          , e = r.md5(a)
                          , a = [];
                        return a.push("data=" + t),
                        a.push("property=0"),
                        a.push("salt=" + e),
                        a.push("width=162"),
                        "//qrcode.iqiyipic.com/login/?" + a.join("&")
                    }
                }
            })
        }
        .call(n, a, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, a(0))
}
, function(t, n, b) {
    (function(y) {
        var e = function(e, t, n) {
            var i = b(6)
              , o = b(2)
              , s = b(5)
              , a = b(1)
              , r = b(62)
              , c = b(4)
              , d = b(8)
              , l = b(17)
              , u = b(9)
              , p = new (b(63))
              , h = b(64);
            window.lib = window.lib || {},
            window.lib.__callbacks__ = window.lib.__callbacks__ || {};
            var g = "请稍后重试"
              , f = {
                "weixin": {
                    "w": 500,
                    "h": 470,
                    "type": 29,
                    "rseat": "wx"
                },
                "qq": {
                    "w": 600,
                    "h": 400,
                    "type": 4,
                    "rseat": "qq"
                },
                "weibo": {
                    "w": 600,
                    "h": 400,
                    "type": 2,
                    "rseat": "wb"
                },
                "zhifubao": {
                    "w": 650,
                    "h": 620,
                    "type": 5,
                    "rseat": "zfb"
                },
                "baidu": {
                    "w": 600,
                    "h": 400,
                    "type": 1,
                    "rseat": "bd"
                },
                "mi": {
                    "w": 900,
                    "h": 685,
                    "type": 30,
                    "rseat": "xm"
                }
            }
              , m = {
                "1": {
                    "type": "weixin"
                },
                "2": {
                    "type": "qq"
                },
                "3": {
                    "type": "weibo"
                },
                "4": {
                    "type": "zhifubao"
                },
                "5": {
                    "type": "baidu"
                },
                "6": {
                    "type": "mi"
                }
            }
              , v = null;
            n.exports = y.Class("thridPartyLoginAction", {
                "extend": i,
                "construct": function(e) {
                    this.panel = e.panel,
                    this.types = e.types || "1,2,3,4,5,6",
                    this.toastPanel = e.toastPanel,
                    this.verifyCenter = e.verifyCenter,
                    this.business = e.business,
                    this.thirdLoginCB = e.thirdLoginCB,
                    this.rpage = "passsdk"
                },
                "methods": {
                    "init": function() {
                        this.render(),
                        this.bindEvent(),
                        this.cbData = ""
                    },
                    "bindEvent": function() {
                        var t = this;
                        window.lib.__callbacks__["_oAuthSuccess"] = function(e) {
                            t.handleAuthSuc(e)
                        }
                        ,
                        v = function(e) {
                            e = e.data;
                            e && "__loginSdkAuthSuccess" === e.type && t.handleAuthSuc(e.data)
                        }
                        ,
                        window.addEventListener && window.addEventListener("message", v);
                        for (var e = this.panel.querySelectorAll("[data-thirdparty]"), n = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            l.isAgree() && (e = (e = (e = e || window.event).target || e.srcElement) && e.getAttribute("data-thirdparty"),
                            "pca" == t.business ? t.callPCA(e) : t.thirdLoginCB ? t.specialCallPage(e) : t.callThirdLogin(e),
                            c.fire({
                                "type": "setUpdateInfo",
                                "data": {
                                    "updateInfo": !1
                                }
                            }))
                        }, i = 0; i < e.length; i++)
                            a.on(e[i], "click", n)
                    },
                    "render": function() {
                        var t = [];
                        this.types.split(",").forEach(function(e) {
                            t.push(m[e])
                        });
                        var e = this.renderHtml(h, {
                            "lists": t
                        });
                        this.panel.innerHTML = e
                    },
                    "callPCA": function(e) {
                        var e = f[e]
                          , t = this.getThirdLoginUrl(e.type);
                        try {
                            var n = '{"call_type":"request", "cmd":"third_login", "cmd_context":"", "cmd_data":' + JSON.stringify({
                                "thirdurl": t
                            }) + "}";
                            window.external.js_app_service(n)
                        } catch (i) {}
                    },
                    "specialCallPage": function(e) {
                        var t = f[e]
                          , n = this.getThirdLoginUrl(t.type)
                          , i = this.getWinConfig(e);
                        try {
                            window[this.thirdLoginCB]({
                                "type": "open",
                                "data": {
                                    "url": n,
                                    "config": i
                                }
                            })
                        } catch (o) {}
                    },
                    "getWinConfig": function(e) {
                        e = f[e];
                        return e.l = window.screenX + (window.screen.width - e.w) / 2,
                        e.t = window.screenY + (window.screen.height - e.h) / 2,
                        "height=" + e.h + ",width=" + e.w + ",top=" + e.t + ",left=" + e.l + ",toolbar=no,menubar=no,scrollbars=no, resizable=yes,location=yes, status=no"
                    },
                    "callThirdLogin": function(e) {
                        var t = f[e]
                          , n = this.getWinConfig(e)
                          , e = this.getThirdLoginUrl(t.type);
                        this.snsWindow = r.href("__window", {
                            "url": e,
                            "config": n
                        }),
                        d.click({
                            "rpage": "passsdk",
                            "block": this.block,
                            "rseat": this.block + "_" + t.rseat
                        }),
                        this.selectType = t.rseat
                    },
                    "getThirdLoginUrl": function(e) {
                        var t = o.getConfig()
                          , n = "https://www.iqiyi.com/thirdlogin/close.html";
                        "pca" == this.business ? (n = window.location.origin + "/thirdlogin/close.html",
                        n += "?business=pca") : this.thirdLoginCB && (n += "?thirdLoginCB=" + this.thirdLoginCB);
                        t = {
                            "type": e,
                            "isiframe": 1,
                            "_pos": 1,
                            "agenttype": t.agenttype,
                            "verifyPhone": 1,
                            "ptid": t.ptid,
                            "fromSDK": 1,
                            "is_reg_confirm": 1,
                            "sdk_version": "1.0.0",
                            "exception_url": n,
                            "success_url": n
                        },
                        n = s.thirdLogin;
                        return n += "?" + a.jsonToQuery(t)
                    },
                    "handleAuthSuc": function(e) {
                        e = e || {};
                        var t = ""
                          , n = "";
                        this.snsWindow && this.snsWindow.close(),
                        n = "object" == typeof e ? (t = a.getQueryValue(e.url, "msg") || e.msg,
                        a.getQueryValue(e.url, "code") || e.code) : (t = a.getQueryValue(e, "msg") || "",
                        a.getQueryValue(e, "code") || "");
                        var i = y.cookie.get("P00038") || t
                          , i = decodeURIComponent(i)
                          , t = y.cookie.get("P00037") || n
                          , n = y.cookie.get("P00036") || e.data
                          , e = y.cookie.get("P00001") && y.cookie.get("P00002") && y.cookie.get("P00003");
                        if (this.cbData = n,
                        "A00000" == t || e)
                            c.fire({
                                "type": "handleLoginSuc",
                                "data": {
                                    "rpage": "login_scs_3_" + this.selectType
                                }
                            });
                        else if ("P00807" == t) {
                            var o = "";
                            if (this.cbData)
                                try {
                                    o = JSON.parse(decodeURIComponent(this.cbData)).token
                                } catch (s) {}
                            o = decodeURIComponent(o),
                            c.fire({
                                "type": "toggleLoginTypes",
                                "data": {
                                    "type": 5,
                                    "token": o,
                                    "rpage": "login_scs_3_" + this.selectType
                                }
                            })
                        } else
                            "P01118" == t ? this.regConfirm() : "P00908" == t ? c.fire({
                                "type": "showQrCodeLogin",
                                "data": {
                                    "type": "lock",
                                    "mobile": i
                                }
                            }) : (this.showErr(i),
                            window.MITO && window.MITO.log({
                                "message": "handleAuthSuc三方登录回调失败",
                                "data": {
                                    "code": t,
                                    "msg": i,
                                    "data": n
                                }
                            }))
                    },
                    "regConfirm": function(e) {
                        var n = this
                          , t = ""
                          , i = y.cookie.get("P00036") || n.cbData;
                        if (i) {
                            i = decodeURIComponent(i);
                            try {
                                t = JSON.parse(i).token
                            } catch (s) {}
                        }
                        var o = {
                            "token": e,
                            "regToken": t
                        };
                        p.regConfirm(o, function(e) {
                            var t;
                            "A00000" == e.code ? c.fire({
                                "type": "handleLoginSuc",
                                "data": {
                                    "rpage": "login_scs_3_" + n.selectType,
                                    "isNewUser": !0
                                }
                            }) : "P00223" == e.code ? ((t = o).ErrCb = function() {
                                n.showErr(g),
                                window.MITO && window.MITO.log({
                                    "message": "三方注册确认接口触发验证中心失败",
                                    "data": o
                                })
                            }
                            ,
                            n.verifyCenter.callSDK(e, t, function(e) {
                                e ? n.regConfirm(e) : n.showErr(g)
                            })) : "P00807" == e.code ? (c.fire({
                                "type": "toggleLoginTypes",
                                "data": {
                                    "type": 5,
                                    "rpage": "login_scs_3_" + n.selectType
                                }
                            }),
                            c.fire({
                                "type": "setUpdateInfo",
                                "data": {
                                    "updateInfo": !0
                                }
                            })) : (n.showErr(e.msg || g),
                            window.MITO && window.MITO.log({
                                "message": "regConfirm三方注册确认接口失败",
                                "data": e
                            }))
                        })
                    },
                    "showErr": function(e, t) {
                        u.showTip(this.toastPanel, {
                            "tip": e,
                            "btnTip": t || "使用其他账号登录"
                        })
                    },
                    "destroy": function() {
                        window.addEventListener && v && (window.removeEventListener("message", v),
                        v = null)
                    },
                    "sendBlock": function(e, t) {
                        this.block = 1 == e ? "acc_3" : 2 == e ? "QR_3" : "sms_3",
                        d.block({
                            "rpage": this.rpage,
                            "block": this.block
                        }),
                        this.parentPanel = t
                    }
                }
            })
        }
        .call(n, b, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, b(0))
}
, function(e, t, n) {
    t = function(e, t, n) {
        var i = {
            "href": function(e, t) {
                var n = "string" == typeof t ? t : t.url;
                if ("__blank" == e)
                    window.open(n, "_blank");
                else {
                    if ("__window" == e) {
                        t = t.config || "",
                        t = window.open(n, "newwindow", t);
                        return t || alert("请允许弹窗验证窗体。"),
                        t
                    }
                    "__self" == e ? window.location.href = n : n === window.parent.location.href ? window.parent.location.reload() : window.parent.location.href = n
                }
            }
        };
        n.exports = i
    }
    .call(t, n, t, e);
    t === undefined || (e.exports = t)
}
, function(t, n, d) {
    (function(c) {
        var e = function(e, t, n) {
            var i = d(7)
              , s = d(1)
              , a = d(10)
              , o = d(5)
              , r = d(2);
            n.exports = c.Class("thridPartyLoginService", {
                "construct": function() {
                    this._remoteInterface = new i({
                        "regConfirm": {
                            "url": o.userRegConfirm
                        }
                    })
                },
                "methods": {
                    "regConfirm": function(e, t) {
                        var n = this
                          , i = r.getConfig()
                          , o = {
                            "agenttype": i.agenttype,
                            "app_version": i.appVersion || "",
                            "device_id": i.deviceid || c.cookie.get("QC005") || "",
                            "dfp": "",
                            "fromSDK": i.fromSDK,
                            "ptid": i.ptid,
                            "reg_confirm_token": e.regToken,
                            "sdk_version": i.sdk_version,
                            "serviceId": 2,
                            "token": e.token || ""
                        };
                        a.getDFP(function(e) {
                            o.dfp = e,
                            s.isCors() && (o.qd_sc = c.md5(decodeURIComponent(s.jsonToQuery(o)) + "tS7BdPLU2w0JD89dh")),
                            n._remoteInterface.send({
                                "ifname": "regConfirm",
                                "param": o,
                                "needMd5": !0
                            }, function(e) {
                                t && t(e)
                            })
                        })
                    }
                }
            })
        }
        .call(n, d, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, d(0))
}
, function(e, t) {
    e.exports = '<div class="sns-title">其他方式登录</div> <div class="sns-list"> {{each lists as item}} <a href="javascript:;" class="icon-login icon-login__{{item.type}}" data-thirdparty="{{item.type}}"></a> {{/each}} </div>'
}
, function(t, n, b) {
    (function(y) {
        var e = function(e, t, n) {
            var i = b(6)
              , o = b(24)
              , s = b(66)
              , a = new (b(67))
              , r = b(1)
              , c = b(4)
              , d = b(3)
              , l = b(26)
              , u = b(8)
              , p = b(13)
              , h = b(17)
              , g = b(68)
              , f = b(71)
              , m = "smsLoginRegAcodeChange"
              , v = "resetSmsLoginRegBtnStatus";
            n.exports = y.Class("smsLoginRegAction", {
                "extend": i,
                "construct": function(e) {
                    this.panel = e.panel,
                    this.types = e.types || "",
                    this.verifyCenter = e.verifyCenter,
                    this.upSmsCodePanel = e.upSmsCodePanel,
                    this.verifyPhonePanel = e.verifyPhonePanel,
                    this.doms = {},
                    this.nameKit = null,
                    this.areaIns = null,
                    this.sendTimer = null,
                    this.isNewUser = !1,
                    this.type = e.type || "login",
                    this.hideBack = e.hideBack || !1,
                    this.bindToken = e.token || "",
                    this.rpage = "login" == this.type ? "passsdk" : "reg" == this.type ? "signup" : "authentication_1",
                    this.block = "login" == this.type ? "psprt_sms" : "reg" == this.type ? "signup_click" : "authentication_1",
                    this.loginSucRpage = e.loginSucRpage
                },
                "methods": {
                    "init": function() {
                        this.render(),
                        this.bindEvent()
                    },
                    "bindEvent": function() {
                        this.initArea(),
                        this.initNameInput(),
                        this.handleCodeInput(),
                        this.handleBtn(),
                        this.handleSendCodeBtn()
                    },
                    "render": function() {
                        var e = this.renderHtml(s, {
                            "type": this.type,
                            "hideBack": this.hideBack,
                            "noBaseLogin": this.types.indexOf(1) < 0
                        });
                        this.panel.innerHTML = e,
                        this.doms = {
                            "loginBtn": this.panel.querySelector('[data-smsLoginReg="loginBtn"]'),
                            "areaPanel": this.panel.querySelector('[data-smsLoginReg="area"]'),
                            "nameErr": this.panel.querySelector('[data-smsLoginReg="nameErr"]'),
                            "nameInput": this.panel.querySelector('[data-smsLoginReg="nameInput"]'),
                            "codeInput": this.panel.querySelector('[data-smsLoginReg="codeInput"]'),
                            "codeErr": this.panel.querySelector('[data-smsLoginReg="codeErr"]'),
                            "sendCodeBtn": this.panel.querySelector('[data-smsLoginReg="sendCode"]'),
                            "baseLoginBtn": this.panel.querySelector('[data-smsLoginReg="baseLogin"]'),
                            "back": this.panel.querySelector('[data-smsLoginReg="back"]')
                        }
                    },
                    "showPanel": function(e) {
                        this.show(e || this.panel)
                    },
                    "initArea": function() {
                        this.areaIns = new o({
                            "panel": this.doms.areaPanel,
                            "fireName": m
                        }),
                        this.areaIns.render()
                    },
                    "handleCodeInput": function() {
                        var t = this
                          , n = this.doms.codeInput;
                        this.codeFocus = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.hideCodeErr()
                        }
                        ,
                        r.on(n, "click", this.codeFocus),
                        this.codeBlur = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            0 == n.value.trim().length && (n.value = "")
                        }
                        ,
                        r.on(n, "blur", this.codeBlur),
                        this.checkValidate = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.hideCodeErr(),
                            t.setLoginBtnStatus()
                        }
                        ,
                        r.on(n, "keyup", this.checkValidate),
                        r.on(n, "input", this.checkValidate)
                    },
                    "setLoginBtnStatus": function() {
                        var e = this.nameKit.checkNameValidate()
                          , t = 6 == this.doms.codeInput.value.trim().length
                          , n = this.doms.loginBtn;
                        e && t ? d.removeClass(n, "btn-gray") : d.addClass(n, "btn-gray")
                    },
                    "showCodeErr": function(e) {
                        this.doms.codeErr.innerHTML = e,
                        d.removeClass(this.doms.codeErr, "dn")
                    },
                    "hideCodeErr": function() {
                        d.addClass(this.doms.codeErr, "dn")
                    },
                    "initNameInput": function() {
                        var e = this;
                        this.nameKit = new l({
                            "name": this.doms.nameInput,
                            "nameErr": this.doms.nameErr,
                            "zoneKey": this.acode,
                            "fireEnableName": v,
                            "zoneChangeFireName": m
                        }),
                        this.nameKit.init(),
                        c.on(v, function() {
                            e.setLoginBtnStatus()
                        })
                    },
                    "handleBtn": function() {
                        var t = this;
                        this.btnCli = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            h.isAgree() && ("realname" == t.type ? (u.click({
                                "rpage": t.rpage,
                                "block": t.block,
                                "rseat": "authentication_login"
                            }),
                            t.validatePhone()) : (t.authcodeLogin(),
                            u.click({
                                "rpage": t.rpage,
                                "block": t.block,
                                "rseat": "login" == t.type ? "sms_login" : "signup_click"
                            })))
                        }
                        ,
                        r.on(this.doms.loginBtn, "click", this.btnCli),
                        this.doms.baseLoginBtn ? r.on(this.doms.baseLoginBtn, "click", function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            u.click({
                                "rpage": t.rpage,
                                "block": t.block,
                                "rseat": "sms2acc"
                            }),
                            c.fire({
                                "type": "toggleLoginTypes",
                                "data": {
                                    "type": 1
                                }
                            })
                        }) : this.doms.back && (this.backcli = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.hide(t.panel),
                            c.fire({
                                "type": "backShow",
                                "data": {
                                    "resetShowPanel": "realname" != t.type,
                                    "resetSize": !0
                                }
                            }),
                            "realname" == t.type && t.unBindEvent()
                        }
                        ,
                        r.on(this.doms.back, "click", this.backcli)),
                        "realname" == this.type && (c.on("realnameErr", function(e) {
                            e.data.msg && t.nameKit.showErrMsg(e.data.msg)
                        }),
                        c.on("realnameClear", function() {
                            t.clearPanel()
                        }))
                    },
                    "authcodeLogin": function(e) {
                        var t = this
                          , n = this.doms.loginBtn;
                        !e && d.hasClass(n, "btn-gray") || (n = t.doms.nameInput.value.trim(),
                        e = e || t.doms.codeInput.value.trim(),
                        n = {
                            "phone": n,
                            "acode": t.areaIns.getAcode().acode,
                            "authCode": e
                        },
                        t.hideCodeErr(),
                        t.nameKit.clearErrMsg(),
                        p.number(e) ? a.authcodeLogin(n, function(e) {
                            "A00000" == e.code ? (e.data.isNewUser = t.isNewUser,
                            e.data.rpage = t.isNewUser ? "signup_scs" : "login_scs_sms",
                            e.data.isReg = "reg" == t.type,
                            c.fire({
                                "type": "handleLoginSuc",
                                "data": e.data
                            })) : "P00159" == e.code || "A00006" == e.code || "P00402" == e.code ? t.nameKit.showErrMsg(e.msg) : t.showCodeErr(e.msg)
                        }) : t.showCodeErr("验证码不匹配"))
                    },
                    "validatePhone": function(e) {
                        var t, n, i = this, o = this.doms.loginBtn;
                        !e && d.hasClass(o, "btn-gray") || (t = i.doms.nameInput.value.trim(),
                        o = i.doms.codeInput.value.trim(),
                        n = {
                            "phone": t,
                            "acode": i.areaIns.getAcode().acode,
                            "authCode": e || o,
                            "token": i.bindToken
                        },
                        a.validate(n, function(e) {
                            var t;
                            i.hideCodeErr(),
                            i.nameKit.clearErrMsg(),
                            "A00000" == e.code ? (n.panel = i.verifyPhonePanel,
                            n.prePanel = i.panel,
                            n.preRpage = i.rpage,
                            n.preBlock = i.block,
                            n.loginSucRpage = i.loginSucRpage,
                            t = {
                                "verifyPhoneResult": e.data.verifyPhoneResult,
                                "validateData": n
                            },
                            f.identify(t)) : "P00159" == e.code || "A00006" == e.code ? i.nameKit.showErrMsg(e.msg) : i.showCodeErr(e.msg)
                        }))
                    },
                    "handleSendCodeBtn": function() {
                        var t = this
                          , n = this.doms.sendCodeBtn
                          , i = this.doms.nameInput;
                        this.sendCodeCli = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            d.hasClass(n, "send-again") || (0 != (e = i.value.trim()).length ? t.nameKit.checkNameValidate() && h.isAgree() && ("realname" == t.type ? t._sendSmsCode() : t._checkAccount({
                                "phone": e,
                                "acode": t.areaIns.getAcode().acode
                            })) : t.nameKit.showPhoneMsg())
                        }
                        ,
                        r.on(n, "click", this.sendCodeCli)
                    },
                    "_checkAccount": function(e) {
                        var t = this;
                        a.checkAccount(e, function(e) {
                            "A00000" == e.code ? (t.isNewUser = !e.data,
                            t._sendSmsCode()) : "P00404" == e.code || "P00105" == e.code ? t._sendSmsCode() : (t.nameKit.showPhoneMsg(e.msg),
                            d.hasClass(t.doms.codeErr, "dn") || t.hideCodeErr())
                        })
                    },
                    "_sendSmsCode": function(e) {
                        var n = this
                          , i = {
                            "phone": this.doms.nameInput.value.trim(),
                            "acode": n.areaIns.getAcode().acode,
                            "token": e,
                            "requestType": "realname" == n.type ? 26 : 22
                        };
                        a.secureSendCode(i, function(e) {
                            var t;
                            "A00000" == e.code ? n._ecountDown() : "P00223" == e.code ? (clearInterval(n.sendTimer),
                            (t = i).ErrCb = function() {
                                n.nameKit.showPhoneMsg("请稍后重试"),
                                window.MITO && window.MITO.log({
                                    "message": "短信登录注册：发短信接口触发验证中心失败",
                                    "data": i
                                })
                            }
                            ,
                            n.verifyCenter.callSDK(e, t, function(e) {
                                e ? n._sendSmsCode(e) : n.nameKit.showPhoneMsg("请稍后重试")
                            })) : "P00174" == e.code ? n.showSmsLoginUp() : (n.nameKit.showPhoneMsg(e.msg),
                            d.hasClass(n.doms.codeErr, "dn") || n.hideCodeErr())
                        })
                    },
                    "_ecountDown": function() {
                        var e = this
                          , t = 58
                          , n = this.doms.sendCodeBtn;
                        clearInterval(this.sendTimer),
                        d.addClass(n, "send-again"),
                        n.innerHTML = "重新获取验证码(59秒)",
                        this.sendTimer = setInterval(function() {
                            return n.innerHTML = "重新获取验证码(" + t + "秒)",
                            0 === t ? (clearInterval(e.sendTimer),
                            d.removeClass(n, "send-again"),
                            !(n.innerHTML = "获取验证码")) : void t--
                        }, 1e3)
                    },
                    "showSmsLoginUp": function() {
                        var t = this;
                        this.upSmsCodeIns || (this.upSmsCodeIns = new g({
                            "panel": this.upSmsCodePanel,
                            "type": this.type
                        }));
                        this.upSmsCodeIns.init({
                            "prePanel": this.panel,
                            "phone": this.doms.nameInput.value.trim(),
                            "acode": this.areaIns.getAcode().acode,
                            "aname": this.areaIns.getAcode().name,
                            "requestType": "realname" == this.type ? 26 : 22,
                            "cb": function(e) {
                                "realname" == t.type ? t.validatePhone(e) : t.authcodeLogin(e)
                            }
                        }),
                        this.hide(this.panel)
                    },
                    "unBindEvent": function() {
                        clearInterval(this.sendTimer),
                        r.un(this.doms.codeInput, "click", this.codeFocus),
                        r.un(this.doms.codeInput, "blur", this.codeBlur),
                        r.un(this.doms.codeInput, "keyup", this.checkValidate),
                        r.un(this.doms.codeInput, "input", this.checkValidate),
                        r.un(this.doms.loginBtn, "click", this.btnCli),
                        r.un(this.doms.back, "click", this.backcli),
                        r.un(this.doms.sendCodeBtn, "click", this.sendCodeCli),
                        this.codeFocus = null,
                        this.codeBlur = null,
                        this.checkValidate = null,
                        this.btnCli = null,
                        this.backcli = null,
                        this.sendCodeCli = null
                    },
                    "resetAcode": function(e, t) {
                        this.areaIns.resetAcode(e, t)
                    },
                    "clearPanel": function() {
                        clearInterval(this.sendTimer);
                        var e = this.doms.sendCodeBtn;
                        d.removeClass(e, "send-again"),
                        e.innerHTML = "获取验证码",
                        this.doms.codeInput.value = "",
                        d.addClass(this.doms.codeErr, "dn"),
                        this.doms.nameInput.value = "",
                        d.addClass(this.doms.nameErr, "dn"),
                        d.addClass(this.doms.loginBtn, "btn-gray")
                    }
                }
            })
        }
        .call(n, b, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, b(0))
}
, function(e, t) {
    e.exports = '{{if type == \'login\'}} <div class="qy-login-tab {{if noBaseLogin == true}}single-tab{{/if}}"> <a href="javascript:;" data-smsLoginReg="baseLogin" class="{{if noBaseLogin == true}}dn{{/if}}">密码登录</a> <a href="javascript:;" class="selected">短信登录<span class="tab-line"></span></a> </div> {{else}} <div class="qy-login-title"> <span class="back-link {{if hideBack==true}}dn{{/if}}" data-smsLoginReg="back"> <i class="iconfont icon-back"></i>返回 </span> <div class="title-content no-margin"> <div class="major-desc"> <p>{{if type == \'reg\'}}注册账号{{else}}安全验证{{/if}}</p> </div> <div class="minor-desc"> <p>{{if type == \'realname\'}}为了您的账号安全，请绑定一个手机号{{/if}}</p> </div> </div> </div> {{/if}} <div class="qy-login-field"> <div class="field-item"> <div class="field-error dn" data-smsLoginReg="nameErr"></div> <div class="field-country-code" data-smsLoginReg="area"></div> <div class="field-account"> <input type="text" class="input-box" data-smsLoginReg="nameInput" maxlength="20" placeholder="请输入手机号"> </div> </div> <div class="field-item"> <div class="field-error dn" data-smsLoginReg="codeErr">验证码错误</div> <div class="field-confirm-code"> <input type="text" class="input-box" data-smsLoginReg="codeInput" maxlength="6" placeholder="请输入验证码"> <span class="send-code" data-smsLoginReg="sendCode">获取验证码</span> </div> </div> </div> <div class="qy-login-btn"> <div class="btn-common"> <div class="btn-inner btn-major btn-gray" data-smsLoginReg="loginBtn">{{if type == \'reg\'}}注册{{else}}登录{{/if}} </div> </div> <div class="btn-common btn-minor dn">绑定其他手机号</div> </div>'
}
, function(t, n, l) {
    (function(d) {
        var e = function(e, t, n) {
            var i = l(7)
              , a = l(16)
              , r = l(10)
              , o = l(1)
              , s = l(5)
              , c = l(2);
            n.exports = d.Class("smsLoginService", {
                "construct": function() {
                    this._remoteInterface = new i({
                        "secureSendCode": {
                            "url": s.secureSendCode
                        },
                        "authcodeLogin": {
                            "url": s.authcodeLogin
                        },
                        "validate": {
                            "url": s.validate
                        },
                        "checkAccount": {
                            "url": s.checkAccount
                        }
                    })
                },
                "methods": {
                    "checkAccount": function(e, t) {
                        var n = c.getConfig()
                          , n = {
                            "__NEW": 1,
                            "account": e.phone,
                            "agenttype": n.agenttype,
                            "app_version": n.appVersion || "",
                            "area_code": e.acode,
                            "dfp": "",
                            "fromSDK": n.fromSDK,
                            "lang": "",
                            "ptid": n.ptid,
                            "sdk_version": n.sdk_version
                        };
                        this.cmd5x(n, "checkAccount", t, !1)
                    },
                    "secureSendCode": function(e, t) {
                        var n = c.getConfig()
                          , i = {
                            "__NEW": 1,
                            "agenttype": n.agenttype,
                            "app_version": n.appVersion || "",
                            "area_code": e.acode,
                            "cellphoneNumber": e.phone,
                            "dfp": ""
                        };
                        e.token && (i.env_token = e.token),
                        i.fromSDK = n.fromSDK,
                        i.lang = "",
                        i.nr = 1,
                        i.ptid = n.ptid,
                        i.requestType = e.requestType,
                        i.sdk_version = n.sdk_version,
                        i.serviceId = 2,
                        this.cmd5x(i, "secureSendCode", t, !0)
                    },
                    "authcodeLogin": function(e, t) {
                        var n = c.getConfig()
                          , e = {
                            "__NEW": 1,
                            "agenttype": n.agenttype,
                            "app_version": n.appVersion || "",
                            "area_code": e.acode,
                            "authCode": e.authCode,
                            "cellphoneNumber": e.phone,
                            "dfp": ""
                        };
                        e.fromSDK = n.fromSDK,
                        e.lang = "",
                        e.ptid = n.ptid,
                        e.requestType = 22,
                        e.sdk_version = n.sdk_version,
                        e.serviceId = 2,
                        this.cmd5x(e, "authcodeLogin", t, !1)
                    },
                    "validate": function(e, t) {
                        var n = c.getConfig()
                          , e = {
                            "agenttype": n.agenttype,
                            "app_version": n.appVersion || "",
                            "area_code": e.acode,
                            "authCode": e.authCode,
                            "cellphoneNumber": e.phone,
                            "fromSDK": n.fromSDK,
                            "lang": "",
                            "ptid": n.ptid,
                            "requestType": 26,
                            "sdk_version": n.sdk_version,
                            "serviceId": 2,
                            "token": e.token
                        };
                        this.interfaceSend(e, "validate", t)
                    },
                    "cmd5x": function(t, n, i, o) {
                        var s = this;
                        r.getDFP(function(e) {
                            t.dfp = e,
                            t && o && t.cellphoneNumber && (t.cellphoneNumber = a.rsaFun(t.cellphoneNumber)),
                            s.interfaceSend(t, n, i)
                        })
                    },
                    "interfaceSend": function(e, t, n) {
                        o.isCors() && (e.qd_sc = d.md5(decodeURIComponent(o.jsonToQuery(e)) + "tS7BdPLU2w0JD89dh")),
                        this._remoteInterface.send({
                            "ifname": t,
                            "param": e,
                            "needMd5": !0
                        }, function(e) {
                            n && n(e)
                        })
                    }
                }
            })
        }
        .call(n, l, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, l(0))
}
, function(t, n, d) {
    (function(c) {
        var e = function(e, t, n) {
            var i = d(6)
              , o = d(69)
              , s = new (d(70))
              , a = d(1)
              , r = d(4);
            n.exports = c.Class("upSmsCodeAction", {
                "extend": i,
                "construct": function(e) {
                    this.panel = e.panel,
                    this.type = e.type,
                    this.rpage = "upsms"
                },
                "methods": {
                    "init": function(e) {
                        this.config = e,
                        this.doms = {},
                        this.upToken = "",
                        this.getUpSmsCode(),
                        r.fire({
                            "type": "toggleSpecialPanel",
                            "data": !1
                        })
                    },
                    "bindEvent": function() {
                        var t = this;
                        this.btnClick = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.upStatusTimer()
                        }
                        ,
                        a.on(this.doms.btn, "click", this.btnClick),
                        this.backClick = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.hidePanel()
                        }
                        ,
                        a.on(this.doms.back, "click", this.backClick),
                        a.on(this.doms.modify, "click", this.backClick),
                        this.refreshClick = function(e) {
                            e.stopPropagation && e.stopPropagation(),
                            t.getUpSmsCode(!0),
                            t.hide(t.doms.timeoutCover)
                        }
                        ,
                        a.on(this.doms.refresh, "click", this.refreshClick)
                    },
                    "hidePanel": function() {
                        this.clearResultTimer(),
                        this.unBindEvent(),
                        this.hide(this.panel),
                        r.fire({
                            "type": "toggleSpecialPanel",
                            "data": "login" == this.type || "3"
                        }),
                        this.show(this.config.prePanel)
                    },
                    "unBindEvent": function() {
                        a.un(this.doms.btn, "click", this.btnClick),
                        a.un(this.doms.back, "click", this.backClick),
                        a.un(this.doms.modify, "click", this.backClick),
                        a.un(this.doms.refresh, "click", this.refreshClick),
                        this.btnClick = null,
                        this.backClick = null,
                        this.refreshClick = null
                    },
                    "getUpSmsCode": function(t) {
                        var n = this
                          , i = {
                            "acode": this.config.acode,
                            "phone": this.config.phone,
                            "requestType": this.config.requestType
                        };
                        s.upBizInfo(i, function(e) {
                            "A00000" == e.code && e.data ? (n.upToken = e.data.upToken,
                            t ? (n.doms.serviceNum.innerHTML = e.data.serviceNum,
                            n.doms.content.innerHTML = e.data.content,
                            n.doms.btn.innerHTML = "我已经发送了") : n.render(e.data),
                            n.timeOutControl()) : (n.showCover("系统异常", "重新发送"),
                            window.MITO && window.MITO.log({
                                "message": "up_biz_info.action接口调用失败",
                                "data": i
                            }))
                        })
                    },
                    "render": function(e) {
                        e = this.renderHtml(o, {
                            "aname": this.config.aname,
                            "phone": this.config.phone,
                            "content": e.content,
                            "serviceNum": e.serviceNum
                        });
                        this.panel.innerHTML = e,
                        this.show(this.panel),
                        this.doms = {
                            "modify": this.panel.querySelector('[data-upsmscode="modify"]'),
                            "btn": this.panel.querySelector('[data-upsmscode="btn"]'),
                            "back": this.panel.querySelector('[data-upsmscode="back"]'),
                            "timeoutCover": this.panel.querySelector('[data-upsmscode="timeout"]'),
                            "content": this.panel.querySelector('[data-upsmscode="content"]'),
                            "serviceNum": this.panel.querySelector('[data-upsmscode="serviceNum"]'),
                            "timeoutTitle": this.panel.querySelector('[data-upsmscode="timeoutTitle"]'),
                            "refresh": this.panel.querySelector('[data-upsmscode="refresh"]')
                        },
                        this.bindEvent()
                    },
                    "timeOutControl": function() {
                        var e = this;
                        e.statusTimeout && clearTimeout(e.statusTimeout),
                        e.statusTimeout = setTimeout(function() {
                            e.showCover("已超时，请刷新", "点击刷新")
                        }, 3e5)
                    },
                    "showCover": function(e, t) {
                        this.clearResultTimer(),
                        this.doms.timeoutTitle.innerHTML = e,
                        this.doms.refresh.innerHTML = t,
                        this.show(this.doms.timeoutCover)
                    },
                    "upStatusTimer": function() {
                        var e = this
                          , t = 60;
                        this.statusTimer && clearInterval(this.statusTimer),
                        this.doms.btn.innerHTML = "发送中...",
                        this.statusTimer = setInterval(function() {
                            0 === (t -= 3) ? e.showCover("我们没能收到您的短信", "重新发送") : e.autoCheckResult()
                        }, 3e3)
                    },
                    "clearResultTimer": function() {
                        this.statusTimer && (clearInterval(this.statusTimer),
                        this.statusTimer = null),
                        this.statusTimeout && (clearTimeout(this.statusTimeout),
                        this.statusTimeout = null),
                        this.upToken = ""
                    },
                    "autoCheckResult": function() {
                        var t = this
                          , e = {
                            "acode": this.config.acode,
                            "phone": this.config.phone,
                            "requestType": this.config.requestType,
                            "upToken": this.upToken
                        };
                        s.upBizStatus(e, function(e) {
                            "A00000" == e.code && (t.hidePanel(),
                            t.config.cb(e.data.authCode))
                        })
                    }
                }
            })
        }
        .call(n, d, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, d(0))
}
, function(e, t) {
    e.exports = '<div class="qy-login-title"> <span class="back-link" data-upsmscode="back"> <i class="iconfont icon-back"></i>返回 </span> <div class="title-content"> <div class="major-desc"> <p>编辑短信</p> </div> <div class="minor-desc"> <p>您接收短信验证码次数已达到上限，<br/>请发送短信进行验证</p> </div> </div> </div> <div class="qy-login-msg"> <div class="msg-item"> <span class="msg-name">{{aname}}</span> <span class="msg-info">{{phone}}</span> <a href="javascript:;" class="theme-color" data-upsmscode="modify">修改</a> </div> <div class="msg-item"> <span class="msg-name">请编辑短信</span> <span class="msg-info" data-upsmscode="content">{{content}}</span> </div> <div class="msg-item"> <span class="msg-name">发送到号码</span> <span class="msg-info" data-upsmscode="serviceNum">{{serviceNum}}</span> </div> </div> <div class="qy-login-btn"> <div class="btn-common"> <div class="btn-inner btn-major" data-upsmscode="btn">我已经发送了</div> </div> </div> <div class="qy-login-cover dn" data-upsmscode="timeout"> <div class="qy-cover-align"> <div class="cover-content"> <div class="qy-login-warning"> <i class="iconfont icon-warning"></i> <div class="warning-title" data-upsmscode="timeoutTitle">已超时，请刷新</div> <div class="qy-login-btn"> <div class="btn-common"> <div class="btn-inner btn-major" data-upsmscode="refresh">点击刷新</div> </div> </div> </div> </div> </div> </div>'
}
, function(t, n, l) {
    (function(d) {
        var e = function(e, t, n) {
            var i = l(7)
              , o = l(16)
              , s = l(10)
              , a = l(1)
              , r = l(5)
              , c = l(2);
            n.exports = d.Class("upSmsCodeService", {
                "construct": function() {
                    this._remoteInterface = new i({
                        "upBizInfo": {
                            "url": r.upBizInfo
                        },
                        "upBizStatus": {
                            "url": r.upBizStatus
                        }
                    })
                },
                "methods": {
                    "baseData": function(e) {
                        var t = c.getConfig()
                          , t = {
                            "__NEW": 1,
                            "agenttype": t.agenttype,
                            "app_version": t.appVersion || "",
                            "area_code": e.acode,
                            "cellphoneNumber": o.rsaFun(e.phone),
                            "device_id": t.deviceid || d.cookie.get("QC005") || "",
                            "dfp": "",
                            "fromSDK": t.fromSDK,
                            "lang": "",
                            "ptid": t.ptid,
                            "requestType": e.requestType || 22,
                            "sdk_version": t.sdk_version,
                            "serviceId": 2
                        };
                        return e.upToken && (t.token = e.upToken),
                        t
                    },
                    "upBizInfo": function(e, t) {
                        e = this.baseData(e),
                        this.cmd5x(e, "upBizInfo", t)
                    },
                    "upBizStatus": function(e, t) {
                        e = this.baseData(e),
                        this.cmd5x(e, "upBizStatus", t)
                    },
                    "cmd5x": function(t, n, i) {
                        var o = this;
                        s.getDFP(function(e) {
                            t.dfp = e,
                            a.isCors() && (t.qd_sc = d.md5(decodeURIComponent(a.jsonToQuery(t)) + "tS7BdPLU2w0JD89dh")),
                            o._remoteInterface.send({
                                "ifname": n,
                                "param": t,
                                "needMd5": !0
                            }, function(e) {
                                i && i(e)
                            })
                        })
                    }
                }
            })
        }
        .call(n, l, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, l(0))
}
, function(t, n, i) {
    (function(f) {
        var e = function(e, t, n) {
            var c = i(12)
              , d = i(1)
              , l = i(4)
              , u = i(3)
              , p = i(8)
              , h = i(72)
              , g = new (i(73));
            n.exports = {
                "identify": function(e) {
                    var t = e.verifyPhoneResult
                      , n = e.validateData;
                    "1" == t.newUser ? (e = "1" == t.toBind,
                    this.bindLogin(n, e)) : "1" == t.toBind ? this.directBindPhone(n) : this.verifyAccount(t.name, n)
                },
                "directBindPhone": function(t) {
                    var n = this;
                    t.requestType = 26,
                    g.directBindPhone(t, function(e) {
                        "A00000" == e.code ? l.fire({
                            "type": "handleLoginSuc",
                            "data": {
                                "rpage": t.loginSucRpage
                            }
                        }) : n.showErrPanel(e.msg)
                    })
                },
                "verifyAccount": function(e, t) {
                    var n = this
                      , e = c.compile(h)({
                        "phone": t.phone,
                        "account": e
                    });
                    t.panel.innerHTML = e,
                    u.removeClass(t.panel, "dn"),
                    u.addClass(t.prePanel, "dn");
                    var i = {
                        "rpage": "authentication_2",
                        "block": "authentication_2"
                    };
                    p.block(i),
                    l.fire({
                        "type": "toggleSpecialPanel",
                        "data": !1
                    });
                    var o = t.panel.querySelector('[data-bindphone="login"]')
                      , s = function(e) {
                        e.stopPropagation && e.stopPropagation();
                        e = f.extend({
                            "rseat": "authentication_continue"
                        }, i);
                        p.click(e),
                        g.verifyAccount(t, function(e) {
                            "A00000" == e.code ? l.fire({
                                "type": "handleLoginSuc",
                                "data": {
                                    "rpage": t.loginSucRpage
                                }
                            }) : (d.un(o, "click", s),
                            d.un(a, "click", r),
                            u.addClass(t.panel, "dn"),
                            u.removeClass(t.prePanel, "dn"),
                            n.showErrPanel(e.msg))
                        })
                    };
                    d.on(o, "click", s);
                    var a = t.panel.querySelector('[data-bindphone="back"]')
                      , r = function(e) {
                        e.stopPropagation && e.stopPropagation(),
                        d.un(o, "click", s),
                        d.un(a, "click", r);
                        e = f.extend({
                            "rseat": "authentication_another"
                        }, i);
                        p.click(e),
                        l.fire({
                            "type": "toggleSpecialPanel",
                            "data": "3"
                        }),
                        l.fire({
                            "type": "realnameClear"
                        }),
                        u.addClass(t.panel, "dn"),
                        u.removeClass(t.prePanel, "dn"),
                        p.block({
                            "rpage": t.preRpage,
                            "block": t.preBlock
                        })
                    };
                    d.on(a, "click", r)
                },
                "bindLogin": function(t, n) {
                    var i = this;
                    g.bindLogin(t, function(e) {
                        "A00000" == e.code ? l.fire({
                            "type": "handleLoginSuc",
                            "data": {
                                "rpage": t.loginSucRpage,
                                "isNewUser": n
                            }
                        }) : i.showErrPanel(e.msg)
                    })
                },
                "showErrPanel": function(e) {
                    l.fire({
                        "type": "realnameErr",
                        "data": {
                            "msg": e
                        }
                    })
                }
            }
        }
        .call(n, i, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, i(0))
}
, function(e, t) {
    e.exports = '<div class="qy-login-title"> <div class="title-content align-left"> <div class="major-desc"> <p>安全验证</p> </div> <div class="minor-desc"> <p> 手机号（<span>{{phone}}</span>）已被{{account}}账号绑定，仅可作为本账号的登录身份验证，不能绑定本账号。 </p> </div> </div> </div> <div class="qy-login-btn"> <div class="btn-common"> <div class="btn-inner btn-major" data-bindphone="login">继续登录</div> </div> <div class="btn-common btn-minor" data-bindphone="back">绑定其他手机号</div> </div>'
}
, function(t, n, d) {
    (function(c) {
        var e = function(e, t, n) {
            var i = d(7)
              , s = d(1)
              , a = d(10)
              , o = d(5)
              , r = d(2);
            n.exports = c.Class("bindPhoneService", {
                "construct": function() {
                    this._remoteInterface = new i({
                        "directBindPhone": {
                            "url": o.directBindPhone
                        },
                        "verifyAccount": {
                            "url": o.verifyAccount
                        },
                        "bindLogin": {
                            "url": o.bindLogin
                        }
                    })
                },
                "methods": {
                    "baseData": function(e, t, n) {
                        var i = r.getConfig()
                          , o = {
                            "agenttype": i.agenttype,
                            "app_version": i.appVersion || "",
                            "area_code": e.acode,
                            "authCode": e.authCode,
                            "cellphoneNumber": e.phone,
                            "dfp": ""
                        };
                        o.fromSDK = i.fromSDK,
                        o.lang = "",
                        o.ptid = i.ptid,
                        e.requestType && (o.requestType = e.requestType),
                        o.sdk_version = i.sdk_version,
                        o.serviceId = 2,
                        e.token && (o.token = e.token),
                        a.getDFP(function(e) {
                            o.dfp = e,
                            t && s.isCors() && (o.qd_sc = c.md5(decodeURIComponent(s.jsonToQuery(o)) + "tS7BdPLU2w0JD89dh")),
                            n(o)
                        })
                    },
                    "directBindPhone": function(e, t) {
                        var n = this;
                        this.baseData(e, !1, function(e) {
                            n._send("directBindPhone", e, t, !1)
                        })
                    },
                    "verifyAccount": function(e, t) {
                        var n = this;
                        this.baseData(e, !0, function(e) {
                            n._send("verifyAccount", e, t, !0)
                        })
                    },
                    "bindLogin": function(e, t) {
                        var n = this;
                        this.baseData(e, !0, function(e) {
                            n._send("bindLogin", e, t, !0)
                        })
                    },
                    "_send": function(e, t, n, i) {
                        this._remoteInterface.send({
                            "ifname": e,
                            "param": t,
                            "needMd5": i
                        }, function(e) {
                            n && n(e)
                        })
                    }
                }
            })
        }
        .call(n, d, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, d(0))
}
, function(t, n, o) {
    (function(r) {
        var e = function(e, t, n) {
            var i = o(2)
              , a = o(3);
            n.exports = r.Class("verifyCenterAction", {
                "construct": function(e) {
                    this._instance = null,
                    this.timer = null,
                    this.slideCover = e.slideCover,
                    this.slidePanel = e.slidePanel
                },
                "methods": {
                    "init": function(e) {
                        window.VerifyCenter ? e && "function" == typeof e && e() : (r.load("css", "//security.iqiyi.com/static/v2/verifycenter/css/verifycenter.css"),
                        this.isLoadSuc(e),
                        r.load("js", "//security.iqiyi.com/static/v2/verifycenter/js/verifycenter.js", function() {
                            window.VerifyCenter && e && "function" == typeof e && e()
                        }))
                    },
                    "callSDK": function(t, n, i) {
                        var o = this;
                        this.init(function() {
                            var e;
                            window.VerifyCenter && t.data && t.data.data ? (e = t.data.data,
                            n.token = e.token,
                            3 == e.auth_type && 2 == e.level && 1 == e.secure_page ? o.slideCode(n, i) : 11 == e.auth_type ? o.autoVerify(n, i) : n.ErrCb()) : n.ErrCb()
                        })
                    },
                    "isLoadSuc": function(e) {
                        var t = this;
                        clearTimeout(this.timer),
                        this.timer = setTimeout(function() {
                            clearTimeout(t.timer),
                            window.__newVC || e()
                        }, 5e3)
                    },
                    "slideCode": function(e, t) {
                        var n = this
                          , e = this._getCommonParams(e)
                          , e = r.extend({
                            "callback": function(e) {
                                "A00000" === e.code && (n._instance && (n._instance.remove(),
                                n._instance = null),
                                t(e.token),
                                a.addClass(n.slideCover, "dn"))
                            },
                            "captchaType": "slidecode"
                        }, e);
                        this._instance = new VerifyCenter(e)
                    },
                    "autoVerify": function(e, i) {
                        var o = this
                          , t = this._getCommonParams(e)
                          , s = this.slidePanel
                          , t = r.extend({
                            "callback": function(e) {
                                if ("A00000" === e.code) {
                                    o._instance && (o._instance.remove(),
                                    o._instance = null);
                                    try {
                                        var t = s.children && s.children[0];
                                        s.removeChild(t)
                                    } catch (n) {}
                                    e = e.token || e.data.initData.token;
                                    i(e),
                                    a.addClass(o.slideCover, "dn")
                                }
                            },
                            "triggerElement": e.triggerElement,
                            "bindEvent": "click",
                            "captchaType": "auto",
                            "isShowModalCloseBtn": !0,
                            "ignoreJsBridge": !0,
                            "reportImmediate": !0
                        }, t);
                        this._instance = new VerifyCenter(t)
                    },
                    "_getCommonParams": function(e) {
                        var t = i.getConfig()
                          , n = this
                          , t = {
                            "wrapper": this.slidePanel,
                            "type": !1,
                            "initErrorCallback": function() {
                                e.errCb && e.errCb()
                            },
                            "DomLoadCallback": function() {
                                a.removeClass(n.slideCover, "dn"),
                                n.slidePanel.style.display = "block",
                                e.loadCb && e.loadCb()
                            },
                            "ptid": t.ptid,
                            "agentType": t.agenttype,
                            "deviceId": t.deviceid || r.cookie.get("QC005") || "",
                            "clientVersion": 1,
                            "phoneNumber": e.phone,
                            "areaCode": "" + e.acode || "86",
                            "requestType": e.requestType,
                            "isShowModalCloseBtn": !0,
                            "dfp": t.dfp || window.dfp && dfp.tryGetFingerPrint && dfp.tryGetFingerPrint() || "",
                            "token": e.token,
                            "width": 290,
                            "height": 170
                        };
                        return this._instance && this._instance.remove(),
                        t
                    }
                }
            })
        }
        .call(n, o, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, o(0))
}
, function(t, n, c) {
    (function(r) {
        var e = function(e, t, n) {
            var i = c(5)
              , o = c(2)
              , s = c(27)
              , a = c(7);
            n.exports = {
                "_doSync": function(e) {
                    var t = o.getConfig()
                      , n = t.domain;
                    "iqiyi.com" != n && "pps.tv" != n || (n = {
                        "agenttype": e.agenttype || t.agenttype || "1",
                        "authcookie": r.cookie.get("P00001"),
                        "fromSDK": t.fromSDK || "1",
                        "sdk_version": t.sdk_version || "1.0.0"
                    },
                    e = i.delcookiePPS,
                    /pps/.test(t.domain) && (e = i.delcookieIQIYI),
                    s(e, {
                        "data": n,
                        "sign": !1,
                        "onsuccess": function() {},
                        "onfailure": function() {}
                    }))
                },
                "request": function(e, t) {
                    var n = o.getConfig();
                    this._doSync(e);
                    n = {
                        "agenttype": e.agenttype || n.agenttype || "1",
                        "app_version": n.appVersion || "",
                        "fromSDK": n.fromSDK || "1",
                        "noredirect": 1,
                        "ptid": e.ptid || n.ptid || "01010021010000000000",
                        "sdk_version": n.sdk_version || "1.0.0"
                    };
                    new a({
                        "url": i.logout
                    }).send({
                        "param": n
                    }, function(e) {
                        t && t(e)
                    })
                }
            }
        }
        .call(n, c, n, t);
        e === undefined || (t.exports = e)
    }
    ).call(this, c(0))
}
, function(e, t, i) {
    t = function(e, t, n) {
        var o = i(2)
          , s = i(27)
          , a = (i(10),
        i(5));
        n.exports = {
            "request": function() {
                var e, t, n = o.getConfig(), i = n.domain;
                "iqiyi.com" != i && "pps.tv" != i || (t = e = "",
                t = /pps/.test(i) ? (e = a.ssoTokenPPS,
                a.ssoCookieIQIYI) : (e = a.ssoTokenIQIYI,
                a.ssoCookiePPS),
                i = {
                    "agenttype": n.agenttype,
                    "callback": "callback",
                    "fromSDK": n.fromSDK,
                    "ptid": n.ptid,
                    "sdk_version": n.sdk_version
                },
                s(e, {
                    "data": i,
                    "sign": !0,
                    "onsuccess": function(e) {
                        e && "A00000" == e.code && e.data && e.data.token && (e = {
                            "agenttype": n.agenttype,
                            "callback": "callback",
                            "fromSDK": n.fromSDK,
                            "sdk_version": n.sdk_version,
                            "token": e.data.token
                        },
                        s(t, {
                            "data": e,
                            "sign": !0,
                            "onsuccess": function() {},
                            "onfailure": function() {}
                        }))
                    },
                    "onfailure": function() {}
                }))
            }
        }
    }
    .call(t, i, t, e);
    t === undefined || (e.exports = t)
}
]);
passwd="123456"
kk(passwd)