import { GraphQLClient, GraphQLWebSocketClient } from "graphql-request";
import { getSdk } from "../generated/graphql";

const graphQLClient = new GraphQLClient("http://localhost:8000/graphql");
export const sdk = getSdk(graphQLClient);

export async function createWebSocketClient(url: string) {
  return new Promise<GraphQLWebSocketClient>((resolve) => {
    const socket = new WebSocket(url, "graphql-transport-ws");
    const client: GraphQLWebSocketClient = new GraphQLWebSocketClient(
      socket as unknown as WebSocket,
      { onAcknowledged: async (_p) => resolve(client) }
    );
  });
}
