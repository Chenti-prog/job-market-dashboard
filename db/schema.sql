DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    title TEXT,
    company TEXT,
    description TEXT,
    onsite_remote TEXT,
    salary TEXT,
    location TEXT,
    criteria TEXT,
    posted_date DATE,
    link TEXT,
    region TEXT
);

