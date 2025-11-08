export async function searchMovies(query) {
    if (!query) throw new Error('query is required');
    const url = new URL('/search', window.__BACKEND_URL__ || 'http://localhost:5000');
    url.searchParams.set('query', query);
    const res = await fetch(url.toString(), {
        headers: { 'Accept': 'application/json' },
    });
    if (!res.ok) {
        const err = await res.json().catch(()=>({ message: res.statusText }));
        throw new Error(err.message || 'Request failed');
    }
    const data = await res.json();
    return data.results ?? data;
}