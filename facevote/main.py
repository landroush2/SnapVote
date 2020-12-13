import face_recognition
import os


def find_match(elector_id,image):

    KNOWN_FACES = 'media/elector'
    TOLERANCE = 0.5
    MODEL = 'hog'

    known_faces = []
    known_names = []


    for filename in os.listdir(f"{KNOWN_FACES}/{elector_id}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES}/{elector_id}/{filename}")
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(elector_id)

    locations = face_recognition.face_locations(image,model=MODEL)
    encodings = face_recognition.face_encodings(image,locations)

    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print(f"Match found {match}")
            return True

    return False
