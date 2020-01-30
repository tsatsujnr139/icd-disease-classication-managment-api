from django.core.management.base import BaseCommand, CommandError
import psycopg2


class Command(BaseCommand):
    """django command to load initial dataset from csv file into postgres db"""
    help = ("Loads initial disease classification "
            "dataset from csv file into postgres")

    def handle(self, *args, **options):
        try:
            conn = psycopg2.connect(
                "host=db dbname=icd_diagnosis"
                " user=postgres password=mypassword")
            cur = conn.cursor()
            # cur.execute("""
            #     DROP TABLE IF EXISTS core_diseaseclassification;
            #     CREATE TABLE core_diseaseclassification(
            #     id SERIAL PRIMARY KEY,
            #     classification_standard text,
            #     category_code text,
            #     diagnosis_code text,
            #     full_code text,
            #     abbreviated_description text,
            #     full_description text,
            #     category_title text)
            #     """)
            with open('diagnosis_codes.csv', 'r') as in_file:
                cur.copy_expert(
                    """COPY core_diseaseclassification(
                        classification_standard,
                        category_code,
                        diagnosis_code,
                        full_code,abbreviated_description,
                        full_description,
                        category_title)
                        FROM STDIN WITH (FORMAT CSV)""",
                    in_file)
                conn.commit()
        except CommandError:
            pass
