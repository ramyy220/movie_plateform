export const API_BASE = window.__BACKEND_URL__ || import.meta.env.VITE_API_BASE || 'http://localhost:5000'

export async function discoverMovies({ page = 1, count = 12 } = {}) {
  // const url = new URL('/movies/discover', API_BASE)
  const url = new URL('/discover', API_BASE)
  url.searchParams.set('page', page)
  url.searchParams.set('count', count)
  console.debug('[discoverMovies] url:', url.toString())
  const res = await fetch(url.toString(), { credentials: 'same-origin' })
  const text = await res.text()
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${text}`)
  }
  try {
    const data = JSON.parse(text)
    // si l'API retourne directement un tableau, normaliser
    if (Array.isArray(data)) {
      return { results: data, page, total_pages: 1 }
    }
    return data
  } catch (err) {
    console.error('[discoverMovies] parse error:', err, 'raw:', text)
    throw new Error('Réponse JSON invalide du serveur')
  }
}
export async function nowplayingMovies({ page = 1, count = 12 } = {}) {
    const url = new URL('/movie/now_playing', API_BASE)
    url.searchParams.set('page', page)
    url.searchParams.set('count', count)
    console.debug('[nowplayingMovies] url:', url.toString())
    const res = await fetch(url.toString(), { credentials: 'same-origin' })
    const text = await res.text()
    if (!res.ok) {
      throw new Error(`HTTP ${res.status}: ${text}`)
    }
    try {
      const data = JSON.parse(text)
        // si l'API retourne directement un tableau, normaliser
        if (Array.isArray(data)) {
            return { results: data, page, total_pages: 1 }
        }
        return data
        } catch (err) {
        console.error('[nowplayingMovies] parse error:', err, 'raw:', text)
        throw new Error('Réponse JSON invalide du serveur')
        }
}

export async function moviePopular({ page = 1, count = 12 } = {}) {
    const url = new URL('/movie/popular', API_BASE)
    url.searchParams.set('page', page)
    url.searchParams.set('count', count)
    console.debug('[moviePopular] url:', url.toString())
    const res = await fetch(url.toString(), { credentials: 'same-origin' })
    const text = await res.text()
    if (!res.ok) {
      throw new Error(`HTTP ${res.status}: ${text}`)
    }
    try {
      const data = JSON.parse(text)
        // si l'API retourne directement un tableau, normaliser
        if (Array.isArray(data)) {
            return { results: data, page, total_pages: 1 }
        }
        return data
        }
        catch (err) {   
        console.error('[moviePopular] parse error:', err, 'raw:', text)
        throw new Error('Réponse JSON invalide du serveur')
 }

}

export async function movieTopRated({ page = 1, count = 12 } = {}) {
    const url = new URL('/movie/top_rated', API_BASE)
    url.searchParams.set('page', page)
    url.searchParams.set('count', count)
    console.debug('[movieTopRated] url:', url.toString())
    const res = await fetch(url.toString(), { credentials: 'same-origin' })
    const text = await res.text()
    if (!res.ok) {
      throw new Error(`HTTP ${res.status}: ${text}`)
    }
    try {
      const data = JSON.parse(text)
        // si l'API retourne directement un tableau, normaliser
        if (Array.isArray(data)) {
            return { results: data, page, total_pages: 1 }
        }
        return data
        }
        catch (err) {   
        console.error('[movieTopRated] parse error:', err, 'raw:', text)
        throw new Error('Réponse JSON invalide du serveur')
 }

}


export async function movieUpcoming({ page = 1, count = 12 } = {}) {
    const url = new URL('/movie/upcoming', API_BASE)
    url.searchParams.set('page', page)
    url.searchParams.set('count', count)
    console.debug('[movieUpcoming] url:', url.toString())
    const res = await fetch(url.toString(), { credentials: 'same-origin' })
    const text = await res.text()
    if (!res.ok) {
      throw new Error(`HTTP ${res.status}: ${text}`)
    }
    try {
      const data = JSON.parse(text)
        // si l'API retourne directement un tableau, normaliser
        if (Array.isArray(data)) {
            return { results: data, page, total_pages: 1 }
        }
        return data
        }
        catch (err) {   
        console.error('[movieUpcoming] parse error:', err, 'raw:', text)
        throw new Error('Réponse JSON invalide du serveur')
 }

}
