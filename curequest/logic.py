from db_config import get_db_connection

def find_diseases_by_symptoms(symptom_names):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    format_strings = ','.join(['%s'] * len(symptom_names))
    query = f"""
        SELECT d.disease_id, d.name, d.description, COUNT(*) as match_count
        FROM Disease d
        JOIN Disease_Symptom ds ON d.disease_id = ds.disease_id
        JOIN Symptom s ON s.symptom_id = ds.symptom_id
        WHERE s.name IN ({format_strings})
        GROUP BY d.disease_id
        ORDER BY match_count DESC;
    """
    cursor.execute(query, tuple(symptom_names))
    result = cursor.fetchall()
    conn.close()
    return result
