OUTPUTS := ./output/iOverlander.MX.gpx ./output/iOverlander.US.gpx ./output/iOverlander.CA.gpx

all: $(OUTPUTS)
.PHONY: all

./output/iOverlander.%.gpx: ./import/%/*.gpx
	mkdir -p ./output/
	./pyoverlander.py "$<" > "$@"

clean:
	rm -rfv ./output/
.PHONY: clean

print-osmand-icon-map:
	./pyoverlander.py -m ./import/reference.gpx
.PHONY: print-osmand-icon-map

push: $(OUTPUTS)
	adb push $^ /storage/emulated/0/Android/media/net.osmand.plus/tracks/
.PHONY: push
