INSERT INTO categories (
        id,
        name,
        type,
        is_default,
        is_hidden,
        created_at,
        updated_at,
        organization_id
    )
VALUES (
        'TEMP - CAT-00000000-0000-0000-0000-000000000000',
        'name:text',
        'type:text',
        false,
        false,
        '2023-01-01 00:00:00.000000',
        '2023-01-01 00:00:00.000000',
        'TEMP - ORG-00000000-0000-0000-0000-000000000000'
    );