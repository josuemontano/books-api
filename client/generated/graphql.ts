import { GraphQLClient } from 'graphql-request';
import * as Dom from 'graphql-request/dist/types.dom';
import gql from 'graphql-tag';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
};

export type Author = {
  name: Scalars['String'];
};

export type Book = {
  author: Author;
  description?: Maybe<Scalars['String']>;
  id: Scalars['String'];
  isbn13?: Maybe<Scalars['String']>;
  publisher: Publisher;
  title: Scalars['String'];
};

export type BookConnection = {
  edges: Array<BookEdge>;
  pageInfo: PageInfo;
  totalCount: Scalars['Int'];
};

export type BookEdge = {
  cursor: Scalars['String'];
  node: Book;
};

export type PageInfo = {
  endCursor?: Maybe<Scalars['String']>;
  hasNextPage: Scalars['Boolean'];
  hasPreviousPage: Scalars['Boolean'];
  startCursor?: Maybe<Scalars['String']>;
};

export type Publisher = {
  name: Scalars['String'];
};

export type Query = {
  books: BookConnection;
  health: Scalars['String'];
};


export type QueryBooksArgs = {
  after?: InputMaybe<Scalars['String']>;
  before?: InputMaybe<Scalars['String']>;
  first?: Scalars['Int'];
};

export type Subscription = {
  pi: Scalars['Float'];
};


export type SubscriptionPiArgs = {
  precision?: InputMaybe<Scalars['Int']>;
};

export type GetAllBooksQueryVariables = Exact<{
  first?: InputMaybe<Scalars['Int']>;
}>;


export type GetAllBooksQuery = { books: { totalCount: number, pageInfo: { hasNextPage: boolean, hasPreviousPage: boolean, startCursor?: string | null, endCursor?: string | null }, edges: Array<{ cursor: string, node: { title: string } }> } };

export type GetPiSubscriptionVariables = Exact<{
  precision?: InputMaybe<Scalars['Int']>;
}>;


export type GetPiSubscription = { pi: number };


export const GetAllBooksDocument = gql`
    query getAllBooks($first: Int) {
  books(first: $first) {
    totalCount
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
    edges {
      cursor
      node {
        title
      }
    }
  }
}
    `;
export const GetPiDocument = gql`
    subscription getPi($precision: Int) {
  pi(precision: $precision)
}
    `;

export type SdkFunctionWrapper = <T>(action: (requestHeaders?:Record<string, string>) => Promise<T>, operationName: string, operationType?: string) => Promise<T>;


const defaultWrapper: SdkFunctionWrapper = (action, _operationName, _operationType) => action();

export function getSdk(client: GraphQLClient, withWrapper: SdkFunctionWrapper = defaultWrapper) {
  return {
    getAllBooks(variables?: GetAllBooksQueryVariables, requestHeaders?: Dom.RequestInit["headers"]): Promise<GetAllBooksQuery> {
      return withWrapper((wrappedRequestHeaders) => client.request<GetAllBooksQuery>(GetAllBooksDocument, variables, {...requestHeaders, ...wrappedRequestHeaders}), 'getAllBooks', 'query');
    },
    getPi(variables?: GetPiSubscriptionVariables, requestHeaders?: Dom.RequestInit["headers"]): Promise<GetPiSubscription> {
      return withWrapper((wrappedRequestHeaders) => client.request<GetPiSubscription>(GetPiDocument, variables, {...requestHeaders, ...wrappedRequestHeaders}), 'getPi', 'subscription');
    }
  };
}
export type Sdk = ReturnType<typeof getSdk>;