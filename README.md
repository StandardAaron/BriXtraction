![banner](https://user-images.githubusercontent.com/15215359/122690962-95c9ed80-d1fa-11eb-882a-4f1ef94efb06.jpg)


# BriXtraction


A Coffee Extraction API implemented with [FastAPI](https://fastapi.tiangolo.com/).

This was my first go at a more TDD-centric development process for a personal project (who writes tests when they are messing around, anyway ;)).

 This is just the core calculator, based on these [findings](https://www.researchgate.net/publication/335608684_Converting_Brix_to_TDS_-_An_Independent_Study) (TL;DR: 0.85 is more-or-less acceptable for Brix -> TDS readings*).

Some upcoming features to round this out are:

- SCA-style charts for given extraction data
- OpenCV + OCR analysis to determine brix from an image of an analog meter
- the addition of notes (tasting, coffee names/origins, etc)
- persistance
- a front-end

* Temperature plays a role here, so if we wanted, that data could (should?) be added as well, but for now, anyone with an analog meter should normalize their samples to the same temperature you used when you calibrated the meter (probably ~20c).
