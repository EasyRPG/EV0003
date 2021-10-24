
.PHONY: check init-remotes install-modules update-modules

# default target
check:
	git --version
	jq --version
	sopel --version
	python -c "import dateparser"
	@echo All ok?!

define get_release
	curl --silent "https://api.github.com/repos/sopel-irc/$(1)/releases/latest" | jq -r .tag_name
endef

plugins = sopel-chanlogs sopel-github

init-remotes:
	@$(foreach plugin,$(plugins), \
		git ls-remote plugin-$(plugin) > /dev/null || \
			git remote add -f plugin-$(plugin) https://github.com/sopel-irc/$(plugin).git ;\
	)

install-modules: init-remotes
	@$(foreach plugin,$(plugins), \
		[ -e external/$(plugin) ] || git subtree add --prefix external/$(plugin) plugin-$(plugin) `$(call get_release,$(plugin))` --squash ;\
	)

update-modules: install-modules
	@$(foreach plugin,$(plugins), \
		git subtree pull --prefix external/$(plugin) plugin-$(plugin) `$(call get_release,$(plugin))` --squash ;\
	)
