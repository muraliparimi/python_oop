# these are already **deduplicated** impressions
deduped_impressions = [
    {"impression_id": "imp_1", "event_ts": "2025-05-01T10:00:00Z",
     "user_id": "u1", "session_id": "s1", "campaign_id": "cmp_A"},

    {"impression_id": "imp_2", "event_ts": "2025-05-01T10:00:03Z",
     "user_id": "u1", "session_id": "s1", "campaign_id": "cmp_A"},

    {"impression_id": "imp_3", "event_ts": "2025-05-01T10:02:10Z",
     "user_id": "u2", "session_id": "s2", "campaign_id": "cmp_B"},

    # next-day impressions
    {"impression_id": "imp_4", "event_ts": "2025-05-02T09:01:00Z",
     "user_id": "u3", "session_id": "s3", "campaign_id": "cmp_A"},
]

conversions_sample = [
    # purchase for imp_1 (same user & campaign)
    {"conversion_id": "conv_100", "impression_id": "imp_1",
     "event_ts": "2025-05-01T10:00:05Z", "revenue": 129.00},

    # purchase for imp_4 on the next day
    {"conversion_id": "conv_101", "impression_id": "imp_4",
     "event_ts": "2025-05-02T09:01:30Z", "revenue":  49.00},
]

class 