export const getRepoUri = (user: string, repo: string) => {
    const protocol = location.protocol;
    const host = location.host;
    const repoHref = `${protocol}//${user}@${host}/${repo}.git`;
    return repoHref
}