from database import get_connection

def schedule_interview(candidate_id, date, time, interviewer):
    conn = get_connection()
    conn.execute("""INSERT INTO interviews
        (candidate_id, interview_date, interview_time, interviewer)
        VALUES (?,?,?,?)""", (candidate_id, date, time, interviewer))
    conn.commit()
    conn.close()
    return "Interview scheduled successfully."
