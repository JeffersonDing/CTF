export const formatString = (data: string, options: Record<string, string | undefined>) => {
    return data.replace(/\{\{[^\}]+\}\}/g, (match) => {
        const option = match.slice(2, -2);
        return options[option] ?? "";
    })
}