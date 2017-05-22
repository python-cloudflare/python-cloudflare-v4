""" API core commands for Cloudflare API"""

def api_v4(self):
    """ API core commands for Cloudflare API"""

    # The API commands for /user/
    user(self)
    # The API commands for /zones/
    zones(self)
    zones_settings(self)
    zones_analytics(self)
    zones_firewall(self)
    zones_rate_limits(self)
    # The API commands for /railguns/
    railguns(self)
    # The API commands for /organizations/
    organizations(self)
    # The API commands for /certificates/
    certificates(self)
    # The API commands for /ips/
    ips(self)
    # The API commands for /zones/:zone_id/dnssec
    zones_dnssec(self)
    # The API commands for /zones/:zone_id/ssl
    zones_ssl(self)
    # The API commands for CLB /zones/:zone_id/load_balancers & /user/load_balancers
    zones_load_balancers(self)
    user_load_balancers(self)

def user(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "user",
            self._add_with_auth(base, "user"))
    branch = getattr(self, "user")
    setattr(branch, "billing",
            self._add_unused(base, "user/billing"))
    branch = getattr(getattr(self, "user"), "billing")
    setattr(branch, "history",
            self._add_with_auth(base, "user/billing/history"))
    setattr(branch, "profile",
            self._add_with_auth(base, "user/billing/profile"))
    setattr(branch, "subscriptions",
            self._add_unused(base, "user/billing/subscriptions"))
    branch = getattr(getattr(getattr(self, "user"), "billing"), "subscriptions")
    setattr(branch, "apps",
            self._add_with_auth(base, "user/billing/subscriptions/apps"))
    setattr(branch, "zones",
            self._add_with_auth(base, "user/billing/subscriptions/zones"))
    setattr(getattr(self, "user"), "firewall",
            self._add_unused(base, "user/firewall"))
    branch = getattr(getattr(self, "user"), "firewall")
    setattr(branch, "access_rules",
            self._add_unused(base, "user/firewall/access_rules"))
    branch = getattr(getattr(getattr(self, "user"), "firewall"), "access_rules")
    setattr(branch, "rules",
            self._add_with_auth(base, "user/firewall/access_rules/rules"))
    branch = getattr(self, "user")
    setattr(branch, "organizations",
            self._add_with_auth(base, "user/organizations"))
    setattr(branch, "invites",
            self._add_with_auth(base, "user/invites"))
    setattr(branch, "virtual_dns",
            self._add_with_auth(base, "user/virtual_dns"))
    setattr(branch, "subscriptions",
            self._add_with_auth(base, "user/subscriptions"))

def zones(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "zones",
            self._add_with_auth(base, "zones"))
    branch = getattr(self, "zones")
    setattr(branch, "activation_check",
            self._add_with_auth(base, "zones", "activation_check"))
    setattr(branch, "available_plans",
            self._add_with_auth(base, "zones", "available_plans"))
    setattr(branch, "available_rate_plans",
            self._add_with_auth(base, "zones", "available_rate_plans"))
    setattr(branch, "custom_certificates",
            self._add_with_auth(base, "zones", "custom_certificates"))
    branch = getattr(getattr(self, "zones"), "custom_certificates")
    setattr(branch, "prioritize",
            self._add_with_auth(base, "zones", "custom_certificates/prioritize"))
    branch = getattr(self, "zones")
    setattr(branch, "custom_pages",
            self._add_with_auth(base, "zones", "custom_pages"))
    setattr(branch, "dns_records",
            self._add_with_auth(base, "zones", "dns_records"))
    setattr(branch, "keyless_certificates",
            self._add_with_auth(base, "zones", "keyless_certificates"))
    setattr(branch, "pagerules",
            self._add_with_auth(base, "zones", "pagerules"))
    setattr(branch, "purge_cache",
            self._add_with_auth(base, "zones", "purge_cache"))
    setattr(branch, "railguns",
            self._add_with_auth(base, "zones", "railguns"))
    branch = getattr(getattr(self, "zones"), "dns_records")
    setattr(branch, "export",
            self._add_with_auth(base, "zones", "dns_records", "export"))
    branch = getattr(getattr(self, "zones"), "railguns")
    setattr(branch, "diagnose",
            self._add_with_auth(base, "zones", "railguns", "diagnose"))
    branch = getattr(self, "zones")
    setattr(branch, "subscription",
            self._add_with_auth(base, "zones", "subscription"))
    setattr(branch, "subscriptions",
            self._add_with_auth(base, "zones", "subscriptions"))

def zones_settings(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = getattr(self, "zones")
    setattr(branch, "settings",
            self._add_with_auth(base, "zones", "settings"))
    branch = getattr(getattr(self, "zones"), "settings")
    setattr(branch, "advanced_ddos",
            self._add_with_auth(base, "zones", "settings/advanced_ddos"))
    setattr(branch, "always_online",
            self._add_with_auth(base, "zones", "settings/always_online"))
    setattr(branch, "browser_cache_ttl",
            self._add_with_auth(base, "zones", "settings/browser_cache_ttl"))
    setattr(branch, "browser_check",
            self._add_with_auth(base, "zones", "settings/browser_check"))
    setattr(branch, "cache_level",
            self._add_with_auth(base, "zones", "settings/cache_level"))
    setattr(branch, "challenge_ttl",
            self._add_with_auth(base, "zones", "settings/challenge_ttl"))
    setattr(branch, "development_mode",
            self._add_with_auth(base, "zones", "settings/development_mode"))
    setattr(branch, "email_obfuscation",
            self._add_with_auth(base, "zones", "settings/email_obfuscation"))
    setattr(branch, "hotlink_protection",
            self._add_with_auth(base, "zones", "settings/hotlink_protection"))
    setattr(branch, "ip_geolocation",
            self._add_with_auth(base, "zones", "settings/ip_geolocation"))
    setattr(branch, "ipv6",
            self._add_with_auth(base, "zones", "settings/ipv6"))
    setattr(branch, "minify",
            self._add_with_auth(base, "zones", "settings/minify"))
    setattr(branch, "mirage",
            self._add_with_auth(base, "zones", "settings/mirage"))
    setattr(branch, "mobile_redirect",
            self._add_with_auth(base, "zones", "settings/mobile_redirect"))
    setattr(branch, "origin_error_page_pass_thru",
            self._add_with_auth(base, "zones", "settings/origin_error_page_pass_thru"))
    setattr(branch, "polish",
            self._add_with_auth(base, "zones", "settings/polish"))
    setattr(branch, "prefetch_preload",
            self._add_with_auth(base, "zones", "settings/prefetch_preload"))
    setattr(branch, "response_buffering",
            self._add_with_auth(base, "zones", "settings/response_buffering"))
    setattr(branch, "rocket_loader",
            self._add_with_auth(base, "zones", "settings/rocket_loader"))
    setattr(branch, "security_header",
            self._add_with_auth(base, "zones", "settings/security_header"))
    setattr(branch, "security_level",
            self._add_with_auth(base, "zones", "settings/security_level"))
    setattr(branch, "server_side_exclude",
            self._add_with_auth(base, "zones", "settings/server_side_exclude"))
    setattr(branch, "sort_query_string_for_cache",
            self._add_with_auth(base, "zones", "settings/sort_query_string_for_cache"))
    setattr(branch, "ssl",
            self._add_with_auth(base, "zones", "settings/ssl"))
    setattr(branch, "tls_client_auth",
            self._add_with_auth(base, "zones", "settings/tls_client_auth"))
    setattr(branch, "true_client_ip_header",
            self._add_with_auth(base, "zones", "settings/true_client_ip_header"))
    setattr(branch, "tls_1_2_only",
            self._add_with_auth(base, "zones", "settings/tls_1_2_only"))
    setattr(branch, "tls_1_3",
            self._add_with_auth(base, "zones", "settings/tls_1_3"))
    # setattr(branch, "tlsadd_auth",
    #         self._add_with_auth(base, "zones", "settings/tlsadd_auth"))
    # setattr(branch, "trueadd_ip_header",
    #         self._add_with_auth(base, "zones", "settings/trueadd_ip_header"))
    setattr(branch, "websockets",
            self._add_with_auth(base, "zones", "settings/websockets"))
    setattr(branch, "waf",
            self._add_with_auth(base, "zones", "settings/waf"))
    setattr(branch, "http2",
            self._add_with_auth(base, "zones", "settings/http2"))
    setattr(branch, "pseudo_ipv4",
            self._add_with_auth(base, "zones", "settings/pseudo_ipv4"))
    setattr(branch, "opportunistic_encryption",
            self._add_with_auth(base, "zones", "settings/opportunistic_encryption"))
    setattr(branch, "automatic_https_rewrites",
            self._add_with_auth(base, "zones", "settings/automatic_https_rewrites"))

def zones_analytics(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = getattr(self, "zones")
    setattr(branch, "analytics",
            self._add_unused(base, "zones", "analytics"))
    branch = getattr(getattr(self, "zones"), "analytics")
    setattr(branch, "colos",
            self._add_with_auth(base, "zones", "analytics/colos"))
    setattr(branch, "dashboard",
            self._add_with_auth(base, "zones", "analytics/dashboard"))

def zones_firewall(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = getattr(self, "zones")
    setattr(branch, "firewall",
            self._add_unused(branch, "zones", "firewall"))
    branch = getattr(getattr(self, "zones"), "firewall")
    setattr(branch, "access_rules",
            self._add_unused(base, "zones", "firewall/access_rules"))
    setattr(branch, "waf",
            self._add_unused(base, "zones", "firewall/waf"))
    branch = getattr(getattr(getattr(self, "zones"), "firewall"), "waf")
    setattr(branch, "packages",
            self._add_with_auth(base, "zones", "firewall/waf/packages"))
    branch = getattr(getattr(getattr(getattr(self, "zones"), "firewall"), "waf"), "packages")
    setattr(branch, "groups",
            self._add_with_auth(base, "zones", "firewall/waf/packages", "groups"))
    setattr(branch, "rules",
            self._add_with_auth(base, "zones", "firewall/waf/packages", "rules"))
    branch = getattr(getattr(getattr(self, "zones"), "firewall"), "access_rules")
    setattr(branch, "rules",
            self._add_with_auth(base, "zones", "firewall/access_rules/rules"))

def zones_rate_limits(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = getattr(self, "zones")
    setattr(branch, "rate_limits",
            self._add_with_auth(base, "zones", "rate_limits"))

def railguns(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "railguns",
            self._add_with_auth(base, "railguns"))
    branch = getattr(self, "railguns")
    setattr(branch, "zones",
            self._add_with_auth(base, "railguns", "zones"))

def organizations(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "organizations",
            self._add_with_auth(base, "organizations"))
    branch = getattr(self, "organizations")
    setattr(branch, "members",
            self._add_with_auth(base, "organizations", "members"))
    setattr(branch, "invite",
            self._add_with_auth(base, "organizations", "invite"))
    setattr(branch, "invites",
            self._add_with_auth(base, "organizations", "invites"))
    setattr(branch, "railguns",
            self._add_with_auth(base, "organizations", "railguns"))
    branch = getattr(getattr(self, "organizations"), "railguns")
    setattr(branch, "zones",
            self._add_with_auth(base, "organizations", "railguns", "zones"))
    branch = getattr(self, "organizations")
    setattr(branch, "roles",
            self._add_with_auth(base, "organizations", "roles"))
    setattr(branch, "firewall",
            self._add_unused(base, "organizations", "firewall"))
    branch = getattr(getattr(self, "organizations"), "firewall")
    setattr(branch, "access_rules",
            self._add_unused(base, "organizations", "firewall/access_rules"))
    branch = getattr(getattr(getattr(self, "organizations"), "firewall"), "access_rules")
    setattr(branch, "rules",
            self._add_with_auth(base, "organizations", "firewall/access_rules/rules"))
    branch = getattr(self, "organizations")
    setattr(branch, "virtual_dns",
            self._add_with_auth(base, "organizations", "virtual_dns"))

def certificates(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "certificates",
            self._add_with_cert_auth(base, "certificates"))

def ips(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    setattr(self, "ips",
            self._add_noauth(base, "ips"))

def zones_dnssec(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = getattr(self, "zones")
    setattr(branch, "dnssec",
            self._add_with_auth(base, "zones", "dnssec"))

def zones_ssl(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = getattr(self, "zones")
    setattr(branch, "ssl",
            self._add_unused(base, "zones", "ssl"))
    branch = getattr(getattr(self, "zones"), "ssl")
    setattr(branch, "analyze",
            self._add_with_auth(base, "zones", "ssl/analyze"))
    setattr(branch, "certificate_packs",
            self._add_with_auth(base, "zones", "ssl/certificate_packs"))
    setattr(branch, "verification",
            self._add_with_auth(base, "zones", "ssl/verification"))

def zones_load_balancers(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = getattr(self, "zones")
    setattr(branch, "load_balancers",
            self._add_with_auth(base, "zones", "load_balancers"))

def user_load_balancers(self):
    """ API core commands for Cloudflare API"""

    base = self._base
    branch = getattr(self, "user")
    setattr(branch, "load_balancers",
            self._add_unused(base, "user/load_balancers"))
    branch = getattr(getattr(self, "user"), "load_balancers")
    setattr(branch, "monitors",
            self._add_with_auth(base, "user/load_balancers/monitors"))
    setattr(branch, "pools",
            self._add_with_auth(base, "user/load_balancers/pools"))
    branch = getattr(getattr(getattr(self, "user"), "load_balancers"), "pools")

