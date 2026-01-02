import { NextRequest } from 'next/server';
import { cookies } from 'next/headers';

// Handle all HTTP methods for health endpoint
export async function GET(request: NextRequest) {
  return handleRequest(request, 'GET');
}

export async function POST(request: NextRequest) {
  return handleRequest(request, 'POST');
}

export async function PUT(request: NextRequest) {
  return handleRequest(request, 'PUT');
}

export async function PATCH(request: NextRequest) {
  return handleRequest(request, 'PATCH');
}

export async function DELETE(request: NextRequest) {
  return handleRequest(request, 'DELETE');
}

async function handleRequest(request: NextRequest, method: string) {
  try {
    // Get the backend URL from environment variables
    const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';

    // Get the path from the URL
    const pathname = request.nextUrl.pathname; // This will be /health, /docs, or /openapi.json
    const searchParams = request.nextUrl.search;

    // Construct the full backend URL
    let backendApiUrl = `${backendUrl}${pathname}`;
    if (searchParams) {
      backendApiUrl += searchParams;
    }

    // Get the auth token from cookies (Better Auth stores it in cookies)
    const allCookies = await cookies();
    const authCookie = allCookies.get('better-auth.session_token');
    const authHeader = authCookie ? `Bearer ${authCookie.value}` : null;

    // Get request body if present
    let body = null;
    if (method !== 'GET' && method !== 'HEAD') {
      body = await request.json().catch(() => null);
    }

    // Prepare headers for the backend request
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (authHeader) {
      headers['Authorization'] = authHeader;
    }

    console.log(`Proxying ${method} request to: ${backendApiUrl}`);

    // Forward the request to the backend
    const backendResponse = await fetch(backendApiUrl, {
      method,
      headers,
      body: body ? JSON.stringify(body) : undefined,
    });

    // Return the response from the backend
    const responseText = await backendResponse.text();

    return new Response(responseText, {
      status: backendResponse.status,
      headers: {
        'Content-Type': 'application/json',
        ...Object.fromEntries(backendResponse.headers.entries()),
      },
    });
  } catch (error) {
    console.error('API Proxy Error:', error);
    return new Response(
      JSON.stringify({ error: 'Backend service unavailable' }),
      {
        status: 503,
        headers: { 'Content-Type': 'application/json' }
      }
    );
  }
}