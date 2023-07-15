MODULE := image_background_changer_api 

run:
	@python -m $(MODULE)

test:
	@pytest

.PHONY: clean test

clean:
	  rm -rf .pytest_cache .coverage coverage.xml