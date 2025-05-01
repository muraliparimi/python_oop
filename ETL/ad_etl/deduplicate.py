# Inputs

impressions_sample = [
    # campaign A – user u1
    {"impression_id": "imp_1", "event_ts": "2025-05-01T10:00:00Z",
     "user_id": "u1", "session_id": "s1", "campaign_id": "cmp_A"},

    {"impression_id": "imp_2", "event_ts": "2025-05-01T10:00:03Z",
     "user_id": "u1", "session_id": "s1", "campaign_id": "cmp_A"},

    # exact / near duplicate – same impression_id, later timestamp
    {"impression_id": "imp_2", "event_ts": "2025-05-01T10:00:04Z",
     "user_id": "u1", "session_id": "s1", "campaign_id": "cmp_A"},

    # campaign B – user u2
    {"impression_id": "imp_3", "event_ts": "2025-05-01T10:02:10Z",
     "user_id": "u2", "session_id": "s2", "campaign_id": "cmp_B"},
]



def deduplicate_impressions(imps: list[dict]) -> list[dict]:
    impressions = {}
    for impression_detail in imps:
        if impression_detail["impression_id"] not in impressions:
            impressions[impression_detail["impression_id"]] = impression_detail
        else:
            if impressions[impression_detail["impression_id"]]["event_ts"] > impression_detail["event_ts"]:
                impressions[impression_detail["impression_id"]] = impression_detail

    return sorted(list(impressions.values()), key=lambda d: d["event_ts"])


if __name__ == '__main__':
    print(deduplicate_impressions(impressions_sample))
