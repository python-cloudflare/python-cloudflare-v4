""" API core commands for CloudFlare API"""

def api_v4(self):
    """ API core commands for CloudFlare API"""

    # The API commands for /user/
    setattr(self, "user",
            self.add_with_auth(self.base, "user"))
    user = getattr(self, "user")
    setattr(user, "billing",
            self.add_unused(self.base, "user/billing"))
    user_billing = getattr(user, "billing")
    setattr(user_billing, "history",
            self.add_with_auth(self.base, "user/billing/history"))
    setattr(user_billing, "profile",
            self.add_with_auth(self.base, "user/billing/profile"))
    setattr(user_billing, "subscriptions",
            self.add_unused(self.base, "user/billing/subscriptions"))
    user_billing_subscriptions = getattr(user_billing, "subscriptions")
    setattr(user_billing_subscriptions, "apps",
            self.add_with_auth(self.base, "user/billing/subscriptions/apps"))
    setattr(user_billing_subscriptions, "zones",
            self.add_with_auth(self.base, "user/billing/subscriptions/zones"))
    setattr(user, "firewall",
            self.add_unused(self.base, "user/firewall"))
    user_firewall = getattr(user, "firewall")
    setattr(user_firewall, "access_rules",
            self.add_unused(self.base, "user/firewall/access_rules"))
    user_firewall_access_rules = getattr(user_firewall, "access_rules")
    setattr(user_firewall_access_rules, "rules",
            self.add_with_auth(self.base, "user/firewall/access_rules/rules"))
    setattr(user, "organizations",
            self.add_with_auth(self.base, "user/organizations"))
    setattr(user, "invites",
            self.add_with_auth(self.base, "user/invites"))
    setattr(user, "virtual_dns",
            self.add_with_auth(self.base, "user/virtual_dns"))

    # The API commands for /zones/
    setattr(self, "zones",
            self.add_with_auth(self.base, "zones"))
    zones = getattr(self, "zones")
    setattr(zones, "activation_check",
            self.add_with_auth(self.base, "zones", "activation_check"))
    setattr(zones, "available_plans",
            self.add_with_auth(self.base, "zones", "available_plans"))
    setattr(zones, "custom_certificates",
            self.add_with_auth(self.base, "zones", "custom_certificates"))
    zones_custom_certificates = getattr(zones, "custom_certificates")
    setattr(zones_custom_certificates, "prioritize",
            self.add_with_auth(self.base, "zones", "custom_certificates/prioritize"))
    setattr(zones, "custom_pages",
            self.add_with_auth(self.base, "zones", "custom_pages"))
    setattr(zones, "dns_records",
            self.add_with_auth(self.base, "zones", "dns_records"))
    setattr(zones, "keyless_certificates",
            self.add_with_auth(self.base, "zones", "keyless_certificates"))
    setattr(zones, "pagerules",
            self.add_with_auth(self.base, "zones", "pagerules"))
    setattr(zones, "purge_cache",
            self.add_with_auth(self.base, "zones", "purge_cache"))
    setattr(zones, "railguns",
            self.add_with_auth(self.base, "zones", "railguns"))
    zones_railguns = getattr(zones, "railguns")
    setattr(zones_railguns, "diagnose",
            self.add_with_auth(self.base, "zones", "railguns", "diagnose"))
    setattr(zones, "settings",
            self.add_with_auth(self.base, "zones", "settings"))
    zones_settings = getattr(zones, "settings")
    setattr(zones_settings, "advanced_ddos",
            self.add_with_auth(self.base, "zones", "settings/advanced_ddos"))
    setattr(zones_settings, "always_online",
            self.add_with_auth(self.base, "zones", "settings/always_online"))
    setattr(zones_settings, "browser_cache_ttl",
            self.add_with_auth(self.base, "zones", "settings/browser_cache_ttl"))
    setattr(zones_settings, "browser_check",
            self.add_with_auth(self.base, "zones", "settings/browser_check"))
    setattr(zones_settings, "cache_level",
            self.add_with_auth(self.base, "zones", "settings/cache_level"))
    setattr(zones_settings, "challenge_ttl",
            self.add_with_auth(self.base, "zones", "settings/challenge_ttl"))
    setattr(zones_settings, "development_mode",
            self.add_with_auth(self.base, "zones", "settings/development_mode"))
    setattr(zones_settings, "email_obfuscation",
            self.add_with_auth(self.base, "zones", "settings/email_obfuscation"))
    setattr(zones_settings, "hotlink_protection",
            self.add_with_auth(self.base, "zones", "settings/hotlink_protection"))
    setattr(zones_settings, "ip_geolocation",
            self.add_with_auth(self.base, "zones", "settings/ip_geolocation"))
    setattr(zones_settings, "ipv6",
            self.add_with_auth(self.base, "zones", "settings/ipv6"))
    setattr(zones_settings, "minify",
            self.add_with_auth(self.base, "zones", "settings/minify"))
    setattr(zones_settings, "mirage",
            self.add_with_auth(self.base, "zones", "settings/mirage"))
    setattr(zones_settings, "mobile_redirect",
            self.add_with_auth(self.base, "zones", "settings/mobile_redirect"))
    setattr(zones_settings, "origin_error_page_pass_thru",
            self.add_with_auth(self.base, "zones", "settings/origin_error_page_pass_thru"))
    setattr(zones_settings, "polish",
            self.add_with_auth(self.base, "zones", "settings/polish"))
    setattr(zones_settings, "prefetch_preload",
            self.add_with_auth(self.base, "zones", "settings/prefetch_preload"))
    setattr(zones_settings, "response_buffering",
            self.add_with_auth(self.base, "zones", "settings/response_buffering"))
    setattr(zones_settings, "rocket_loader",
            self.add_with_auth(self.base, "zones", "settings/rocket_loader"))
    setattr(zones_settings, "security_header",
            self.add_with_auth(self.base, "zones", "settings/security_header"))
    setattr(zones_settings, "security_level",
            self.add_with_auth(self.base, "zones", "settings/security_level"))
    setattr(zones_settings, "server_side_exclude",
            self.add_with_auth(self.base, "zones", "settings/server_side_exclude"))
    setattr(zones_settings, "sort_query_string_for_cache",
            self.add_with_auth(self.base, "zones", "settings/sort_query_string_for_cache"))
    setattr(zones_settings, "ssl",
            self.add_with_auth(self.base, "zones", "settings/ssl"))
    setattr(zones_settings, "tls_1_2_only",
            self.add_with_auth(self.base, "zones", "settings/tls_1_2_only"))
    setattr(zones_settings, "tlsadd_auth",
            self.add_with_auth(self.base, "zones", "settings/tlsadd_auth"))
    setattr(zones_settings, "trueadd_ip_header",
            self.add_with_auth(self.base, "zones", "settings/trueadd_ip_header"))
    setattr(zones_settings, "waf",
            self.add_with_auth(self.base, "zones", "settings/waf"))
    setattr(zones, "analytics",
            self.add_unused(self.base, "zones", "analytics"))
    zones_analytics = getattr(zones, "analytics")
    setattr(zones_analytics, "colos",
            self.add_with_auth(self.base, "zones", "analytics/colos"))
    setattr(zones_analytics, "dashboard",
            self.add_with_auth(self.base, "zones", "analytics/dashboard"))
    setattr(zones, "firewall",
            self.add_unused(self.base, "zones", "firewall"))
    zones_firewall = getattr(zones, "firewall")
    setattr(zones_firewall, "access_rules",
            self.add_unused(self.base, "zones", "firewall/access_rules"))
    setattr(zones_firewall, "waf",
            self.add_unused(self.base, "zones", "firewall/waf"))
    zones_firewall_waf = getattr(zones_firewall, "waf")
    setattr(zones_firewall_waf, "packages",
            self.add_with_auth(self.base, "zones", "firewall/waf/packages"))
    zones_firewall_waf_packages = getattr(zones_firewall_waf, "packages")
    setattr(zones_firewall_waf_packages, "groups",
            self.add_with_auth(self.base, "zones", "firewall/waf/packages", "groups"))
    setattr(zones_firewall_waf_packages, "rules",
            self.add_with_auth(self.base, "zones", "firewall/waf/packages", "rules"))
    zones_firewall_access_rules = getattr(zones_firewall, "access_rules")
    setattr(zones_firewall_access_rules, "rules",
            self.add_with_auth(self.base, "zones", "firewall/access_rules/rules"))

    # The API commands for /railguns/
    setattr(self, "railguns",
            self.add_with_auth(self.base, "railguns"))
    railguns = getattr(self, "railguns")
    setattr(railguns, "zones",
            self.add_with_auth(self.base, "railguns", "zones"))

    # The API commands for /organizations/
    setattr(self, "organizations",
            self.add_with_auth(self.base, "organizations"))
    organizations = getattr(self, "organizations")
    setattr(organizations, "members",
            self.add_with_auth(self.base, "organizations", "members"))
    setattr(organizations, "invite",
            self.add_with_auth(self.base, "organizations", "invite"))
    setattr(organizations, "invites",
            self.add_with_auth(self.base, "organizations", "invites"))
    setattr(organizations, "railguns",
            self.add_with_auth(self.base, "organizations", "railguns"))
    organizations_railguns = getattr(organizations, "railguns")
    setattr(organizations_railguns, "zones",
            self.add_with_auth(self.base, "organizations", "railguns", "zones"))
    setattr(organizations, "roles",
            self.add_with_auth(self.base, "organizations", "roles"))
    setattr(organizations, "firewall",
            self.add_unused(self.base, "organizations", "firewall"))
    organizations_firewall = getattr(organizations, "firewall")
    setattr(organizations_firewall, "access_rules",
            self.add_unused(self.base, "organizations", "firewall/access_rules"))
    organizations_firewall_access_rules = getattr(organizations_firewall, "access_rules")
    setattr(organizations_firewall_access_rules, "rules",
            self.add_with_auth(self.base, "organizations", "firewall/access_rules/rules"))
    setattr(organizations, "virtual_dns",
            self.add_with_auth(self.base, "organizations", "virtual_dns"))

    # The API commands for /certificates/
    setattr(self, "certificates",
            self.add_with_cert_auth(self.base, "certificates"))

    # The API commands for /ips/
    setattr(self, "ips",
            self.add_noauth(self.base, "ips"))

    # The DNSSEC commands
    setattr(zones, "dnssec",
            self.add_with_auth(self.base, "zones", "dnssec"))

    # EXTRAS
    # /zones/:zone_id/ssl/certificate_packs
    setattr(zones, "ssl",
            self.add_unused(self.base, "zones", "ssl"))
    zones_ssl = getattr(zones, "ssl")
    setattr(zones_ssl, "certificate_packs",
            self.add_with_auth(self.base, "zones", "ssl/certificate_packs"))

