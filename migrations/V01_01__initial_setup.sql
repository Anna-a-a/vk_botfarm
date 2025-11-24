CREATE TYPE user_domain AS ENUM ('CANARY', 'REGULAR');
CREATE TYPE user_env AS ENUM ('PROD', 'PREPROD', 'STAGE');

CREATE TABLE users (
    id UUID PRIMARY KEY,
    created_ad TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    login VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    project_id UUID NOT NULL,
    env user_env NOT NULL,
    domain user_domain NOT NULL,
    locktime TIMESTAMP WITH TIME ZONE
);

COMMENT ON TABLE users IS 'Пользователи';
COMMENT ON COLUMN users.created_ad IS 'Дата создания пользователя';
COMMENT ON COLUMN users.login IS 'Почтовый адрес пользователя';
COMMENT ON COLUMN users.password IS 'Пароль пользователя';
COMMENT ON COLUMN users.project_id IS 'UUID проекта, к которому принадлежит пользователь';
COMMENT ON COLUMN users.env IS 'Название окружения';
COMMENT ON COLUMN users.domain IS 'Тип пользователя';
COMMENT ON COLUMN users.locktime IS 'Временная метка';
