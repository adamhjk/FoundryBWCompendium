.PHONY: release clean test help

# Extract version from module.json
VERSION := $(shell jq -r .version module.json)
ZIP_NAME := v$(VERSION).zip
DIR_NAME := FoundryBWCompendium-$(VERSION)

# Default target
.DEFAULT_GOAL := release

help:
	@echo "FoundryBWCompendium Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  release  - Create GitHub release zip file (default)"
	@echo "  clean    - Remove build artifacts and zip files"
	@echo "  test     - Create release and test extraction"
	@echo "  help     - Show this help message"
	@echo ""
	@echo "Current version: $(VERSION)"

release: clean
	@echo "Creating release $(VERSION)..."
	@echo "Building directory structure..."
	@mkdir -p $(DIR_NAME)/packs
	@echo "Copying files..."
	@cp module.json $(DIR_NAME)/
	@cp README.md $(DIR_NAME)/
	@cp packs/*.db $(DIR_NAME)/packs/
	@echo "Creating zip archive..."
	@zip -r -q $(ZIP_NAME) $(DIR_NAME)
	@rm -rf $(DIR_NAME)
	@echo ""
	@echo "✅ Release created: $(ZIP_NAME)"
	@ls -lh $(ZIP_NAME) | awk '{print "   Size: " $$5}'
	@echo "   Files: $$(unzip -l $(ZIP_NAME) | tail -1 | awk '{print $$2}') files"
	@echo ""

clean:
	@echo "Cleaning build artifacts..."
	@rm -rf $(DIR_NAME)
	@rm -rf FoundryBWCompendium-*
	@rm -f v*.zip
	@rm -rf test-extract
	@echo "✅ Clean complete"

test: release
	@echo ""
	@echo "Testing release structure..."
	@mkdir -p test-extract
	@unzip -q $(ZIP_NAME) -d test-extract
	@echo ""
	@echo "📦 Archive contents:"
	@ls -la test-extract/$(DIR_NAME)/ | tail -n +4
	@echo ""
	@echo "📂 Packs directory:"
	@ls -1 test-extract/$(DIR_NAME)/packs/ | wc -l | awk '{print "   " $$1 " compendium files"}'
	@ls -1 test-extract/$(DIR_NAME)/packs/
	@rm -rf test-extract
	@echo ""
	@echo "✅ Test complete - structure verified"
